# Cómo generar los ficheros `_es.cat`

Guía para traducir los datos de Age of Sigmar 4th al español sin romperlos.

Esta es una traducción **NO OFICIAL** y de aficionado del repositorio
[BSData/age-of-sigmar-4th](https://github.com/BSData/age-of-sigmar-4th). No está
afiliada, respaldada ni aprobada por Games Workshop, BSData ni New Recruit. El
contenido de reglas y perfiles es © Games Workshop Limited.

**El aviso legal completo está en el [README](README.md#disclaimer--aviso-legal)
y hay que respetarlo:** proyecto gratuito, sin publicidad ni monetización, sin
logotipos de Games Workshop, con atribución al repositorio original y sin
presentar la traducción como oficial. Si publicas algo derivado de esto, arrastra
el mismo aviso.

## Qué se traduce y qué no

Los `.cat` y `.gst` son XML. Se traduce el **contenido descriptivo** dentro de
`<description>` y `<characteristic>` y, por petición del usuario del 8 de
septiembre de 2026, los **nombres visibles de unidades, armas y habilidades**
registrados en `translations/names/`, incluidas sus manifestaciones y variantes.
También se incluyen hechizos, plegarias, rasgos, artefactos, formaciones y
opciones de Sendero a la Gloria. Las habilidades se mantienen en los
diccionarios `Abilities - *.es.json` de esa carpeta.

```xml
<selectionEntry id="6353-cb84-ac7f-9a15" name="Bull Charge">
  <profiles>
    <profile name="Bull Charge" typeId="907f-a48-6a04-f788">
      <characteristics>
        <characteristic name="Timing" typeId="652c-3d84">Any Charge Phase</characteristic>
        <!--                                              ^^^^^^^^^^^^^^^^ esto sí -->
      </characteristics>
    </profile>
  </profiles>
</selectionEntry>
```

| Se traduce | No se toca |
| --- | --- |
| Texto dentro de `<description>` | Atributos técnicos y nombres no registrados |
| Texto dentro de `<characteristic>` | `id`, `targetId`, `typeId`, `entryId`, `publicationId`, `gameSystemId` |
| `name=` registrado de `selectionEntry`, `selectionEntryGroup`, `profile`, `entryLink`, `infoLink`, `rule` | Nombres de tipos de perfil, categorías y características |
| `value=` registrado de `modifier` solo cuando `field="name"` | `type=`, `field=`, `scope=` y valores de reglas |
| | Orden de atributos, indentación, comillas, saltos de línea |

**La regla que no se puede saltar: los IDs no se traducen.** Las herramientas de
`tools/` no reescriben el XML: sustituyen rangos de texto y nombres autorizados.
`verify-translation.py` exige la equivalencia exacta con los diccionarios para
esos cambios y que todo lo demás sea idéntico al original.

## Requisitos

Python 3.8 o superior. Nada más: sin dependencias, sin `pip install`.

## Los tres pasos

Ejecuta siempre desde la raíz del repositorio.

### 1. Extraer las cadenas

```bash
python tools/extract-text.py "Ogor Mawtribes.cat"
```

Crea `translations/Ogor Mawtribes.es.json` con una entrada por cadena, ordenadas
de la más corta a la más larga (las cortas son etiquetas y momentos: se traducen
rápido):

```json
{
  "_note": "...",
  "_source": "Ogor Mawtribes.cat",
  "Deployment Phase": "",
  "Pick a visible enemy unit within 12\" of this unit to be the target.": ""
}
```

### 2. Rellenar el JSON

Los JSON son los **únicos datos de traducción que se editan a mano**. Los nombres
se mantienen por separado en `translations/names/<ejército>.es.json`, con las
claves inglesas exactas y sus equivalencias. Una clave compartida entre
ejércitos debe tener el mismo valor; el generador rechaza conflictos. Revisar
[GLOSARIO-NOMBRES.md](GLOSARIO-NOMBRES.md) y
[GLOSARIO-HABILIDADES.md](GLOSARIO-HABILIDADES.md) antes de añadir equivalencias.

- **No toques las claves.** Son la cadena inglesa exacta, byte a byte. Si cambias
  una coma, esa cadena deja de encontrarse y se queda sin traducir. Algunas
  llevan caracteres invisibles (guiones no separables, espacios dobles): por eso
  el JSON las trae ya escritas.
- **Valor vacío = se deja en inglés.** Se puede traducir por tandas y volver más
  tarde; nada se rompe por dejar entradas a medias.
- Los saltos de línea van como `\n`; la herramienta los convierte al fin de
  línea del fichero fuente.

### 3. Generar y verificar

```bash
python tools/apply-translation.py "Ogor Mawtribes.cat"   # escribe Ogor Mawtribes_es.cat
python tools/verify-translation.py                       # verifica todos los pares
```

`verify-translation.py` calcula primero los nombres autorizados, vacía el texto
descriptivo y compara el resto **byte a byte**. También contrasta los atributos,
la estructura y cada texto con los diccionarios de prosa y nombres. Un cambio
no autorizado falla con código 1. Ejemplo del formato de salida:

```
OK     Ejemplo_es.cat  (58/58 cadenas traducidas, 100.0%; 5301 atributos verificados)
```

**El `_es.cat` es un artefacto generado: nunca se edita a mano.** Si hay una
errata, se corrige el JSON y se vuelve a ejecutar el paso 3.

## Etiquetas independientes y referencias en la prosa

**Criterio actualizado por petición del usuario (7 de septiembre de 2026):**
las etiquetas independientes de claves, habilidades de arma e ingredientes
también se traducen. Usar las equivalencias de
[GLOSARIO-ETIQUETAS.md](GLOSARIO-ETIQUETAS.md). Se mantienen intactos los
atributos técnicos y las claves inglesas de los JSON. Las expresiones que solo
contienen datos y los nombres propios sin traducción se registran con su
valor original, en lugar de dejarlos vacíos.

Las siguientes pautas se aplican a las referencias dentro de la prosa ya
traducida; no impiden traducir una etiqueta independiente.


Los nombres de unidades, armas y habilidades registrados se sustituyen automáticamente
también **dentro** del texto generado. No hace falta cambiar manualmente sus
referencias en los JSON de prosa: conservar las claves inglesas originales.
Se usan coincidencias completas, sensibles a mayúsculas y de mayor longitud
primero, sin sustituciones encadenadas. Al cambiar un nombre, regenerar todos
los catálogos que lo citan, incluidos bibliotecas y Regimientos de Renombre.

Las órdenes básicas citadas sin perfil local y los títulos de efectos dentro
de la prosa se registran en `Abilities - Rule references.es.json`. Revisar esas
referencias además de los nombres de perfiles: un título puede aparecer solo
entre comillas o como encabezado de un efecto.

Comprobar la cobertura tras actualizar los originales:

```bash
python tools/verify-name-coverage.py
python tools/test-name-translation.py
python tools/verify-translation.py
```

La primera comprobación detecta nombres pendientes de unidades, armas,
manifestaciones, habilidades, reglas, alias y modificadores de nombre, incluso los del sistema
general `.gst`. Las pruebas comprueban que el generador acepta los nombres
registrados y rechaza cambios en identificadores, nombres y prosa no autorizados.

Las referencias a habilidades, hechizos, plegarias y mejoras registradas se
traducen también entre comillas o con marcado. Se mantienen como en el original
los siguientes términos de prosa cuando no figuran en los diccionarios de nombres:

- Palabras clave con marcado `^^...^^`: `**^^Hero^^**`, `**^^Ogor Mawtribes^^**`,
  `**^^Ward (6+)^^**`, `**^^Rampage^^**`.
- Habilidades de arma: `Crit (2 Hits)`, `Crit (Mortal)`, `Companion`,
  `Anti-Monster (+1 Rend)`, `Charge (+1 Damage)`, `Heal (D3)`.
- Nombres de características: `característica de Health`, `de Attacks`, `de Rend`.
- Nombres de artefactos, trofeos y efectos que todavía no se hayan registrado
  al incorporar una actualización de los originales.

Se traducen: todo lo demás, incluidos los términos de reglas que no son nombres
(`pile-in move`, `control score`, `fury level`, `damage points`…).

Una cadena que solo contiene palabras clave también se traduce: por ejemplo,
`**^^Core^^**, **^^Move^^**` pasa a `**^^Básica^^**, **^^Movimiento^^**`.
Un valor vacío indica trabajo pendiente; los datos sin traducción usan el
mismo texto original como valor.

## Glosario acordado

Para que dos personas traduciendo dos ficheros distintos no usen dos palabras
distintas. Amplíalo cuando aparezca un término nuevo.

| Inglés | Español |
| --- | --- |
| hit / wound / save / ward roll | tirada de impacto / de herida / de salvación / de salvaguardia |
| charge / casting / chanting / run roll | tirada de carga / de lanzamiento / de cántico / de correr |
| unmodified roll | tirada sin modificar |
| re-roll | volver a tirar |
| roll off / roll-off | hacer una tirada enfrentada / la tirada enfrentada |
| spell / prayer / manifestation lore | saber de hechizos / de plegarias / de manifestaciones |
| mortal damage | daño mortal |
| damage points | puntos de daño |
| allocated to | asignados a |
| slain | abatida |
| destroyed | destruida |
| set up | colocar |
| in reserve | en reserva |
| battlefield / battlefield edge | campo de batalla / borde del campo de batalla |
| terrain feature | elemento de escenografía |
| objective (marcador) | marcador de objetivo |
| target | objetivo |
| in combat with | en combate con |
| combat range | alcance de combate |
| pile-in move | movimiento de aproximación |
| control score | puntuación de control |
| power level / fury level | nivel de poder / nivel de furia |
| rage dice | dados de ira |
| command / command points | orden / puntos de orden |
| battle round | ronda de batalla |
| for the rest of the turn / phase / battle | durante el resto del turno / de la fase / de la batalla |
| until the start of your next turn | hasta el inicio de tu siguiente turno |
| wholly within 12" of | totalmente a 12" o menos de |
| within 3" of | a 3" o menos de |
| more than 9" from | a más de 9" de |
| visible to | visible para |
| Once Per Turn (Army) | Una vez por turno (ejército) |
| Your Hero Phase | Tu fase de héroe |
| Any Combat Phase | Cualquier fase de combate |
| End of Any Turn | Final de cualquier turno |
| Deployment Phase | Fase de despliegue |
| Reaction: | Reacción: |
| Designer's Note | Nota del diseñador |
| fate point | punto de destino |
| rage dice / fury level | dados de ira / nivel de furia |
| blood tithe point | punto de diezmo de sangre |
| banishment roll / banished | tirada de destierro / desterrado |
| unbinding roll / unbind / unbound | tirada de desvinculación / desvincular / desvinculado |
| underdog | desvalido |
| labours (Lumineth) | trabajos |
| raw ingredients (Mawseeker Gollop) | ingredientes en bruto |
| masked by illusion | enmascarado/a por ilusión |
| hidden among cultists | escondido/a entre los sectarios |
| living landmark (Trugg's Troggherd) | hito viviente |
| outflanking the enemy | flanqueando al enemigo |
| cronies (Ironsunz) | secuaces |
| magic-eater roll | tirada de devoramagia |
| meaty charge roll | tirada de carga suculenta |
| momentum score | puntuación de ímpetu |
| battle scripture / library (runas) | escritura de batalla / reserva |
| empty / full (Cauldron of Blood) | vacía / llena |
| vexed points (Kharadron Overlords) | puntos de irritación |
| creeping overgrowth (Sylvaneth) | maleza reptante |
| overgrown token (Sylvaneth) | marcador de maleza |
| accused / judged / condemned (Nighthaunt) | acusado/a / juzgado/a / condenado/a |
| soul point (Nighthaunt) | punto de alma |
| rally roll / rally point | tirada de reagrupamiento / punto de reagrupamiento |

Fórmulas que se repiten, para copiar tal cual:

- `Pick a visible enemy unit within 12" of this unit to be the target.` →
  `Elige como objetivo una unidad enemiga visible a 12" o menos de esta unidad.`
- `Roll a dice. On a 3+, ...` → `Tira un dado. Con un 3+, ...`
- `Roll a D3. On a 2+, inflict an amount of mortal damage on the target equal to the roll.` →
  `Tira un D3. Con un 2+, inflige al objetivo una cantidad de daño mortal igual al resultado.`

## Repartir el trabajo

Un fichero fuente por persona. El JSON de cada fichero es independiente, así que
dos personas traduciendo dos facciones distintas no se pisan nunca; el único
punto común es el glosario de arriba.

Empieza por el fichero de facción (`Ogor Mawtribes.cat`: rasgos de batalla,
formaciones, artefactos, saberes) antes que por su `- Library.cat`: el de
facción es unas 20 veces más pequeño y sirve para coger el tono.

## Cuando BSData actualiza el fichero original

1. Trae los cambios del repositorio original.
2. Vuelve a ejecutar el paso 1: conserva lo ya traducido, añade solo las cadenas
   nuevas y avisa de las que han desaparecido (las guarda en `_unused` para no
   perder el trabajo si vuelve a cambiar la redacción).
3. Traduce únicamente las entradas nuevas y repite los pasos 2 y 3.

No hay que retraducir nada más.

## Aviso: ids duplicados

El `_es.cat` conserva el `id` del catálogo original, porque los ids no se
traducen. Dos catálogos con el mismo id **no pueden convivir** en la misma
carpeta: el CI de BSData lo marca como duplicado y New Recruit no debe cargar
los dos a la vez.

Usa el `_es.cat` **en lugar** del original, no junto a él. Si algún día se
quiere que coexistan, hay que cambiar el `id` del elemento `<catalogue>` raíz
(solo ese, ninguno de los internos) y su `name`.

## Qué se commitea

- `translations/<fichero>.es.json` — el trabajo de traducción.
- `translations/names/*.es.json` — los nombres visibles autorizados.
- `<fichero>_es.cat` — el artefacto generado, para quien solo quiera descargarlo.

Antes de hacer commit, ejecuta `python tools/verify-translation.py`. Si no dice
`OK`, no lo subas.


## Términos añadidos al completar las bibliotecas

Las traducciones existentes también usan «blanco» para *target*, «atributo»
para *characteristic*, «terreno» para *terrain feature*, «tirada para herir»
para *wound roll* y «repetir la tirada» para *re-roll*. Son equivalentes a las
formas del glosario anterior. Al modificar una regla, mantener una forma
coherente dentro de su texto. La referencia registrada `Heal (X)` se traduce
como `Curar (X)` en el texto generado.

| Inglés | Español |
| --- | --- |
| under orders | bajo órdenes |
| dark sorcery token | ficha de hechicería oscura |
| heat token | ficha de calor |
| zealotry roll | tirada de fanatismo |
| mark (Cities of Sigmar) | presa |
| hunted by the Order | perseguido/a por la Orden |
| scouting ahead | explorando la avanzadilla |
| consecrated | consagrado/a |
| resistance roll | tirada de resistencia |
| soul-bonded charge | protegido vinculado por el alma |
| questmarked | marcado para la misión |
| stored energy dice | dado de energía almacenada |
| beast form | forma bestial |
| sacrifice point | punto de sacrificio |
| ruinous energy point | punto de energía ruinosa |
| in the tunnels below | en los túneles subterráneos |
| drilling beneath the surface | perforando bajo la superficie |
| Regiment of Renown / Regiment of Ghyran | Regimiento de Renombre / Regimiento de Ghyran |
| marked for justice | señalado/a para la justicia |
| swift point / swift move | punto de rapidez / movimiento rápido |
| pre-eminent / overlooked | preeminente / relegado/a |
| oriented target / bewildered target | blanco orientado / blanco desconcertado |
| unknown location / intended destination | ubicación desconocida / destino previsto |
| remediation roll / remediated / contaminated | tirada de remediación / remediado/a / contaminado/a |
| Landmark of Ghyran | hito de Ghyran |
| Ghyranite Concoction | brebaje ghyranita (conservar la clave inglesa si lleva `^^`) |
| bone-tithe point | punto de diezmo de huesos |
| emberstone-enhanced weapon | arma mejorada con piedra ascua |
