---
name: versionamiento-git
description: Guía el flujo de versionamiento con Git para el equipo. Se activa cuando el usuario pide "ayudame con el versionamiento" o similar, y proporciona número de ticket y descripción. Incluye sincronizar main, crear rama, actualizar README y hacer commits en el formato establecido.
---

# Versionamiento Git - Flujo del equipo

## Cuándo activar

Cuando el usuario diga:
- "ayudame con el versionamiento"
- "versionamiento" + número de ticket
- O pase un ticket (ej: "18047 - Nuevos cambios en migración")

## Información requerida (siempre pedir si falta)

1. **Número de ticket** (ej: 18047)
2. **Descripción del ticket** (ej: Nuevos cambios en migración)
3. **Tipo de cambio**: `[FEAT]` para funcionalidades nuevas, `[FIX]` para correcciones/bugs

## Configuración del desarrollador

- **Iniciales**: MP
- **Nombre**: Marlon Pacheco
- **Formato de rama**: MP + número de ticket (ej: MP18047)

---

## Flujo paso a paso

### 1. Sincronizar repositorio

```bash
git checkout main
git pull
```

Traer el código más reciente del fork antes de crear la rama.

### 2. Crear y cambiar a la rama

```bash
git checkout -b {iniciales}18047
```

Reemplazar `18047` por el número del ticket.

### 3. Actualizar README

Ir al final del archivo `README.md` y agregar **antes del último salto de línea**:

```
* **Marlon Pacheco** - [Número del ticket] - [Descripción del ticket]
```

**Ejemplo** para ticket "18047 - Nuevos cambios en migración":
```
* **Marlon Pacheco** - 18047 - Nuevos cambios en migración
```

### 4. Primer commit (solo README)

```bash
git add README.md
git commit -m "[FEAT] {iniciales}18047 - Inicio desarrollo"
```

O con `[FIX]` si aplica:
```bash
git commit -m "[FIX] {iniciales}18047 - Inicio desarrollo"
```

### 5. Cambios del ticket

Aplicar las modificaciones de código, archivos, carpetas (skills, módulos, etc.) según el ticket. Si ya existen, no hacer nada más; ir al paso 6 y usar `git add .`.

### 6. Segundo commit (cambios del ticket)

```bash
git add .
git commit -m "[FEAT] {iniciales}18047 - Nuevos cambios en migración"
```

- Usar **`git add .`** (no agregar archivo por archivo ni carpeta por carpeta). Incluye todo: archivos nuevos, carpetas nuevas (ej. skills, módulos), modificaciones.
- Usar la **descripción exacta del ticket** en el mensaje del segundo commit.
- **No omitir este commit.** Si hay cambios pendientes (carpetas sin seguimiento, archivos modificados, etc.) que pertenecen al ticket, van aquí. Revisar `git status` antes de hacer push.

### 7. Subir la rama

```bash
git push -u origin {iniciales}18047
```

### 8. Generar paquete de cambios (tar.gz)

Ejecutar **después** de los commits, para crear un archivo solo con los archivos modificados:

```bash
# Obtener el SHA del commit "Inicio desarrollo" (primer commit de la rama)
SHA_INICIAL=$(git log --oneline --grep="Inicio desarrollo" -1 --format="%H")
git archive -o {iniciales}18047.tar.gz HEAD $(git diff --name-only ${SHA_INICIAL}^ HEAD)
```

- Reemplazar `18047` por el número del ticket en el nombre del archivo.
- Usar como base el **padre** del commit "Inicio desarrollo" para incluir todos los archivos de la rama (README + cambios del ticket).

### 9. Obtener SHA1 para "Datos de desarrollo"

- **SHA1 inicial**: commit "Inicio desarrollo" (donde se guarda el README). Ejemplo:
  ```bash
  git log --oneline --grep="Inicio desarrollo" -1 --format="%H"
  ```
- **SHA1 final**: último commit de la rama (donde están todos los paquetes):
  ```bash
  git rev-parse HEAD
  ```

---

## Datos de desarrollo (plantilla)

Completar con la información del ticket y los valores de Git.

**Importante sobre SHA1:**
- **SHA1 inicial** = commit "Inicio desarrollo" (primer commit de la rama, donde se guarda el README). No usar el commit base de main ni versionamientos anteriores.
- **SHA1 final** = último commit de la rama (donde están todos los paquetes/cambios).

```
Datos de desarrollo:
Fecha Inicio: [DD/MM/YYYY] (fecha actual)
Documentación Funcional:
Observaciones: Información completa
Modulos:
-

Liberación del requerimiento:
Versionado en: [Nombre del repositorio] (Github)
Commit: {iniciales}[Número] (nombre de la rama)
SHA1 inicial: [SHA del commit "Inicio desarrollo" - primer commit de la rama]
SHA1 final: [SHA del último commit - git rev-parse HEAD]
```

**Ejemplo** para ticket 22089 en rama MP22089:

```
Datos de desarrollo:
Fecha Inicio: 19/03/2026
Documentación Funcional:
Observaciones: Reunion de Capacitacion Portal de Rutas Nonnos Nueva migración
Modulos:
-

Liberación del requerimiento:
Versionado en: PortalRutasFincasNonnos (Github)
Commit: MP22089
SHA1 inicial: a2234e364c5e369f658906b8d29fbff275fd1d96
SHA1 final: cf6faaaab995ad61a18fa335788ec42768ba1646
```

---

## Formato de mensajes de commit

| Momento | Formato | Ejemplo |
|---------|---------|---------|
| Primer commit (solo README) | `[FEAT]\| [FIX] {iniciales}{numero} - Inicio desarrollo` | `[FEAT] MP18047 - Inicio desarrollo` |
| Segundo commit (cambios) | `[FEAT]\| [FIX] {iniciales}{numero} - {Descripción del ticket}` | `[FEAT] MP18047 - Nuevos cambios en migración` |

---

## Resumen rápido

```
main → git pull → git checkout -b {iniciales}{num}
→ Editar README (agregar entrada al final)
→ Commit 1: git add README.md → "[FEAT] {iniciales}{num} - Inicio desarrollo"
→ Hacer cambios del ticket (o ya existen)
→ Commit 2: git add . → "[FEAT] {iniciales}{num} - {Descripción ticket}"
→ git push -u origin {iniciales}{num}
→ git archive -o {iniciales}{num}.tar.gz HEAD $(git diff --name-only $(git log --oneline --grep="Inicio desarrollo" -1 --format="%H")^ HEAD)
→ Completar plantilla "Datos de desarrollo" (SHA1 inicial: commit Inicio desarrollo, SHA1 final: git rev-parse HEAD)
```

---

## Notas

- La rama `main` se mantiene sincronizada con el repositorio original.
- Los cambios y ramas se crean siempre en el fork del equipo.
- El primer commit debe contener **únicamente** el README.
- En el segundo commit va **todo** el resto: `git add .` y commit. Incluye carpetas nuevas, skills, documentación, código — todo lo que pertenezca al ticket.
- **Error frecuente:** Omitir el segundo commit creyendo que "no hay cambios". Revisar `git status`; si hay archivos/carpetas sin seguimiento o modificados (salvo README ya commiteado), deben ir en el segundo commit.
