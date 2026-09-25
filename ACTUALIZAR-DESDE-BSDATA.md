# Cómo actualizar desde BSData y traducir las novedades

Guía para quienes mantienen `age-of-sigmar-4th-es`. Sirve para incorporar
correcciones, nuevas unidades, warscrolls completos y nuevos catálogos del
[proyecto original](https://github.com/BSData/age-of-sigmar-4th).

Git incorpora las reglas y la estructura originales. Después traducimos los
textos y nombres nuevos en los diccionarios JSON y generamos los archivos
españoles. No hace falta volver a traducir todo el proyecto.

Esta traducción es **no oficial y de aficionado**. Conserva la atribución y las
condiciones del [aviso legal del proyecto](README.md#disclaimer--aviso-legal).

## Antes de empezar

Necesitas Git, Python 3.8 o superior y una copia local del fork. No hacen falta
dependencias de Python adicionales. Los ejemplos usan **PowerShell** desde la
raíz del repositorio; cambia esta ruta si tu copia está en otro lugar:

```powershell
Set-Location C:\dev\age-of-sigmar-4th-es
git status --short
git remote -v
python --version
```

Empieza con el directorio de trabajo limpio: `git status --short` no debe mostrar
cambios. Guarda o termina cualquier trabajo anterior antes de integrar novedades.
`origin` debe apuntar al fork español en el que vayas a publicar.

Ejecuta cada paso por separado y revisa su salida. Si un comando falla, resuelve
el error antes de continuar: PowerShell no se detiene automáticamente tras todos
los errores de programas externos.

## 1. Configurar el repositorio original una sola vez

Consulta los remotos con `git remote -v`. Si todavía no existe `upstream`, añádelo:

```powershell
git remote add upstream https://github.com/BSData/age-of-sigmar-4th.git
```

`origin` es el fork español; `upstream` es el proyecto original de BSData.
Si `upstream` ya existe, comprueba su URL y no repitas el comando.

## 2. Revisar e integrar los commits nuevos

Si hay correcciones oficiales adelantadas en el fork, consulta primero
[Erratas pendientes de BSData](docs/erratas-pendientes-upstream.md). Compara
su manifiesto después de `git fetch upstream` y antes del merge; revisa también
los cambios que Git pueda combinar sin conflictos.

```powershell
git switch main
git pull --ff-only origin main
git fetch upstream
git log --oneline HEAD..upstream/main
git diff --stat HEAD...upstream/main
git diff --name-status HEAD...upstream/main
git rev-parse upstream/main
```

Revisa los commits, anota la revisión de BSData y los archivos afectados.
En la lista de archivos, `A` significa añadido, `M` modificado y `D` eliminado.
Si no hay commits nuevos, no hay novedades de BSData que integrar.

```powershell
git merge --no-commit --no-ff upstream/main
```

La integración queda pendiente de commit mientras completas las traducciones.
El merge conserva la relación con el historial original para futuras
actualizaciones. Un mensaje indicando que se ha detenido antes del commit es
normal con estas opciones.

Si hay conflictos, consulta `git status`, resuelve cada archivo y márcalo con
`git add -- "ruta-del-archivo"`. Conserva las herramientas y traducciones del
fork y las actualizaciones de los originales; no elijas una versión completa
a ciegas. Si necesitas cancelar la integración, `git merge --abort` permite
volver al estado anterior al merge; guarda antes cualquier trabajo nuevo de
traducción que quieras conservar.

## 3. Extraer los textos nuevos o modificados

Ejemplo: BSData añade un warscroll a `Stormcast Eternals - Library.cat`.

```powershell
python tools/extract-text.py "Stormcast Eternals - Library.cat"
```

La herramienta actualiza
`translations/Stormcast Eternals - Library.es.json`:

- Conserva las traducciones de las claves que siguen presentes.
- Añade los textos nuevos con valor vacío.
- Aparta en `_unused` las traducciones que han dejado de coincidir con el fuente
  en esa extracción.

Ejecuta la extracción **una vez por cada original añadido o modificado**,
incluidos los `.gst` cuando corresponda. No pases los archivos `_es`.
Revisa el diff del JSON: la herramienta actual no conserva acumulativamente
el historial previo de `_unused` entre extracciones; Git mantiene las versiones
anteriores si necesitas recuperar una traducción.

## 4. Traducir el contenido del JSON

Busca los valores vacíos y rellénalos. Por ejemplo:

```json
"New rule text in English.": "Nuevo texto de regla en español."
```

**La clave inglesa debe quedar exacta**, incluidos espacios invisibles, signos,
marcado y saltos de línea. Cambia únicamente el valor. Mantén el JSON válido:
comas entre entradas y comillas internas escapadas como `\"`.

Si cambia la redacción de una regla, revisa el cambio de significado antes de
reutilizar su traducción anterior. Una distancia, una restricción o una fase
distinta también deben cambiar en español. Registra los datos o nombres propios
que no se traducen con su texto original como valor; no los dejes vacíos.

Sigue [TRADUCIR.md](TRADUCIR.md) y los glosarios existentes, especialmente
[GLOSARIO-ETIQUETAS.md](GLOSARIO-ETIQUETAS.md). Las claves técnicas, identificadores,
referencias y valores de reglas del XML no se traducen manualmente.

## 5. Traducir unidades, armas, habilidades y opciones nuevas

Los nombres visibles se mantienen por separado en `translations/names/`.
Para detectar los que faltan:

```powershell
python tools/verify-name-coverage.py
```

Añade cada equivalencia al diccionario correspondiente:

| Tipo de nombre | Diccionario habitual en `translations/names/` |
| --- | --- |
| Unidades, armas y manifestaciones | `<facción>.es.json` |
| Habilidades, hechizos y plegarias | `Abilities - <facción>.es.json` |
| Menús, opciones y catálogos | `Menus - <facción>.es.json` |

Ejemplo de entrada dentro del objeto JSON:

```json
"New Warrior": "Nuevo guerrero"
```

Consulta [GLOSARIO-NOMBRES.md](GLOSARIO-NOMBRES.md),
[GLOSARIO-HABILIDADES.md](GLOSARIO-HABILIDADES.md) y
[GLOSARIO-MENUS.md](GLOSARIO-MENUS.md). Una clave compartida debe tener la misma
equivalencia en todos los diccionarios; el generador rechaza conflictos.
Registra también los nombres que deban mantenerse iguales.

## 6. Generar las versiones españolas

Para generar un catálogo concreto:

```powershell
python tools/apply-translation.py "Stormcast Eternals - Library.cat"
```

Esto escribe `Stormcast Eternals - Library_es.cat`. **Los archivos `_es.cat`
y `_es.gst` son generados: nunca se editan a mano.** Corrige los JSON y vuelve
a generar si encuentras un error.

Si has cambiado nombres, regenera todos los catálogos: el generador también
traduce sus referencias dentro de otros textos. Este bloque sirve para ello:

```powershell
Get-ChildItem -File |
    Where-Object {
        $_.Extension -in '.cat', '.gst' -and
        $_.BaseName -notlike '*_es'
    } |
    ForEach-Object {
        python tools/apply-translation.py $_.Name
        if ($LASTEXITCODE -ne 0) {
            throw "Error al generar $($_.Name)"
        }
    }
```

### Si aparece un catálogo completo nuevo

Extrae sus textos, completa el nuevo JSON, registra sus nombres y genera su
pareja `_es`. Comprueba que el nuevo archivo español figure en la verificación.
Los archivos nuevos deben añadirse a Git, además de los modificados.

### Si un catálogo se elimina o cambia de nombre

Revisa la correspondencia con su JSON y su archivo `_es`. Retira o adapta los
artefactos antiguos para no distribuir catálogos obsoletos. El verificador
general solo comprueba parejas cuyo original existe: no detecta por sí solo
todos los archivos españoles huérfanos. No borres nombres compartidos sin
comprobar si otros catálogos siguen utilizándolos.

## 7. Verificar el resultado

Ejecuta estos comandos por separado y resuelve cualquier fallo:

```powershell
python tools/verify-name-coverage.py
python tools/test-name-translation.py
python tools/verify-translation.py
```

Antes de publicar, comprueba que:

- La cobertura de nombres indique **0 pendientes**.
- Todas las pruebas del generador pasen.
- Todas las parejas esperadas aparezcan con `OK` y **100 % de cadenas traducidas**.
- Los nuevos warscrolls y reglas tengan una traducción revisada y coherente.

**`OK` no garantiza una traducción completa**: indica que el archivo concuerda
con sus diccionarios y conserva la estructura técnica esperada. Revisa también
el porcentaje. Del mismo modo, no tener valores vacíos no garantiza cobertura
si falta una clave en el JSON.

La validación compara la traducción con el original actualizado; los cambios
técnicos legítimos de BSData se incorporan a ambos. No comprueba la calidad
lingüística ni sustituye una prueba en la aplicación de listas.

## 8. Documentar, hacer commit y publicar

Actualiza [ESTADO-TRADUCCION.md](ESTADO-TRADUCCION.md) con la revisión integrada,
los catálogos afectados y los resultados reales de cobertura y validación.
Actualiza los glosarios si has incorporado terminología nueva.

Revisa los cambios del merge y las traducciones:

```powershell
git status --short
git diff
git diff --cached
```

Añade los archivos existentes modificados y los nuevos catálogos y diccionarios:

```powershell
git add --update
git add -- '*.cat' '*.gst' translations
git diff --cached --stat
git -c core.whitespace=cr-at-eol diff --cached --check
```

Si has creado otros archivos de documentación, añádelos explícitamente también.
La opción `cr-at-eol` permite comprobar el diff respetando los finales de línea
CRLF de los originales. Revisa que no hayas incluido archivos ajenos al trabajo.

```powershell
git commit -m "Integrar novedades de BSData y actualizar traducciones"
git push origin main
git status --short
```

Este mensaje de commit no añade un tráiler de coautoría. El commit cierra el
merge pendiente e incluye originales, diccionarios y artefactos españoles.
El push requiere permisos de escritura en el fork. Si el equipo colabora
mediante ramas y pull requests, crea una rama antes del merge, publica esa rama
y solicita su revisión en lugar de subir directamente a `main`.

Si GitHub rechaza el push porque otra persona ha actualizado `main`, trae e
integra esos cambios, resuelve los conflictos y repite las verificaciones
afectadas. No uses un push forzado para sobrescribir el trabajo de compañeros.

## Qué comunicar al resto del equipo

Al terminar, incluye en el aviso o pull request:

- Revisión de BSData incorporada y commit del fork.
- Catálogos o warscrolls añadidos o corregidos.
- Traducciones nuevas y cambios de terminología relevantes.
- Resultado de las comprobaciones y cualquier trabajo que siga pendiente.

La secuencia para cada actualización es: traer novedades, integrar, extraer,
traducir textos y nombres, generar, verificar y publicar.
