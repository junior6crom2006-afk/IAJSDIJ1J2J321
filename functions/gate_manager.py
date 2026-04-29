import json
from datetime import datetime
import re
from typing import Optional
from .database import Database
import time

class GateManager:
    GATES_FILE = "database/gates.json"
    _gates_cache = None

    @classmethod
    def _load_gates(cls, force=False):
        """Carga los gates desde el disco a la memoria caché"""
        if cls._gates_cache is None or force:
            try:
                with open(cls.GATES_FILE, 'r') as file:
                    cls._gates_cache = json.load(file)
            except (FileNotFoundError, json.JSONDecodeError):
                cls._gates_cache = []
        return cls._gates_cache

    @classmethod
    def get_all_gates(cls):
        """Retorna todos los gates desde el caché"""
        return cls._load_gates()

    @classmethod
    def reload_cache(cls):
        """Fuerza la recarga de los gates desde el disco"""
        return cls._load_gates(force=True)

    @classmethod
    def register_gate(cls, comando, nombre, tipo=None, premium=True, ultima_revision=None):
        """Registra un nuevo gate o actualiza uno existente"""
        if tipo is None:
            tipo = cls.detect_gate_type(nombre)
        
        gates = cls.get_all_gates()
        gate_exists = False
        
        for gate in gates:
            if gate["comando"] == comando:
                gate["nombre"] = nombre
                gate["tipo"] = tipo
                gate["premium"] = premium
                gate["ultima_revision"] = ultima_revision or time.strftime("%Y-%m-%d %H:%M:%S")
                gate_exists = True
                break
        
        if not gate_exists:
            gates.append({
                "comando": comando,
                "nombre": nombre,
                "tipo": tipo,
                "premium": premium,
                "estado": "ON",
                "razon": None,
                "ultima_revision": ultima_revision or time.strftime("%Y-%m-%d %H:%M:%S")
            })
        
        # Actualizar caché y disco
        cls._gates_cache = gates
        try:
            with open(cls.GATES_FILE, 'w') as f:
                json.dump(gates, f, indent=4)
            return True
        except Exception as e:
            print(f"Error al guardar gates: {str(e)}")
            return False

    @classmethod
    def get_gate_info(cls, comando):
        """Obtiene la información del gate desde el caché"""
        gates = cls.get_all_gates()
        for gate in gates:
            if gate["comando"] == comando:
                return gate
        
        return {
            "estado": "OFF",
            "razon": "Gate no registrado",
            "ultima_revision": "N/A"
        }

    @classmethod
    def toggle_gate(cls, comando, estado, razon=None):
        """Prende o apaga un gate y actualiza caché/disco"""
        gates = cls.get_all_gates()
        for gate in gates:
            if gate["comando"] == comando:
                gate["estado"] = "ON" if estado else "OFF"
                gate["razon"] = razon
                gate["ultima_revision"] = datetime.now().strftime("%Y-%m-%d %H:%M:%S")
                
                cls._gates_cache = gates
                try:
                    with open(cls.GATES_FILE, 'w') as file:
                        json.dump(gates, file, indent=4)
                    return gate
                except:
                    return None
        return None

    @staticmethod
    def get_gates_status() -> dict:
        db = Database()
        return db.obtener_conteo_gates()

    @staticmethod
    def update_gate_type(comando, nuevo_tipo):
        """Actualiza el tipo de gate en caché y disco"""
        gates = GateManager.get_all_gates()
        
        found = False
        for gate in gates:
            # Soportar tanto 'cmd' como 'comando' por compatibilidad
            cmd_key = "comando" if "comando" in gate else "cmd"
            if gate.get(cmd_key) == comando:
                gate["tipo"] = nuevo_tipo
                found = True
                break
            
        if found:
            GateManager._gates_cache = gates
            with open(GateManager.GATES_FILE, "w") as f:
                json.dump(gates, f, indent=4)

    @staticmethod
    def detect_gate_type(nombre):
        nombre = nombre.upper()
        
        # Detectar CHARGED
        if '$' in nombre or 'CHARGED' in nombre:
            return "CHARGED"
        
        # Detectar AUTH
        if '[AUTH]' in nombre or 'AUTH' in nombre:
            return "AUTH"
        
        # Detectar CCN
        if '[CCN]' in nombre or 'CCN' in nombre:
            return "CCN"
        
        # Por defecto
        return "CCN"
