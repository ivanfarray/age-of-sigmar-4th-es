# Cómo generar los ficheros `_es.cat`

Guía para traducir los datos de Age of Sigmar 4th al español sin romperlos.

Esta es una traducción **no oficial** y de aficionado del repositorio
[BSData/age-of-sigmar-4th](https://github.com/BSData/age-of-sigmar-4th). No está
afiliada ni respaldada por Games Workshop, BSData ni New Recruit. El contenido de
reglas y perfiles pertenece a Games Workshop.

## Qué se traduce y qué no

Los `.cat` y `.gst` son XML. Solo se traduce el **contenido descriptivo**: el
texto que hay dentro de `<description>` y `<characteristic>`.

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
| Texto dentro de `<description>` | Cualquier atributo, sin excepción |
| Texto dentro de `<characteristic>` | `id`, `targetId`, `typeId`, `entryId`, `publicationId`, `gameSystemId` |
| | `name=` (unidades, armas, habilidades, encabezados) |
| | `type=`, `field=`, `scope=`, `value=` |
| | Orden de atributos, indentación, comillas, saltos de línea |

**La regla que no se puede saltar: los IDs no se traducen.** Las herramientas de
`tools/` no tocan atributos por construcción — no reescriben el XML, localizan
los rangos de bytes del texto y sustituyen solo esos — y `verify-translation.py`
lo comprueba después.

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

Es el **único fichero que se edita a mano**.

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

`verify-translation.py` vacía el texto descriptivo de los dos ficheros y compara
el resto **byte a byte**, además de contrastar los valores de atributo uno por
uno y la estructura. Si algo fuera del texto ha cambiado, falla con código 1 y
dice en qué offset. Salida esperada:

```
OK     Ogor Mawtribes_es.cat  (54/58 cadenas traducidas, 93.1%; 5301 atributos intactos)
```

**El `_es.cat` es un artefacto generado: nunca se edita a mano.** Si hay una
errata, se corrige el JSON y se vuelve a ejecutar el paso 3.

## Qué dejar en inglés dentro de la prosa

Como los `name=` no se traducen, los nombres propios que aparecen **dentro** del
texto también se quedan en inglés. Si no, la regla citaría un nombre que el
jugador no encuentra en ninguna parte del pergamino.

Se quedan en inglés:

- Palabras clave con marcado `^^...^^`: `**^^Hero^^**`, `**^^Ogor Mawtribes^^**`,
  `**^^Ward (6+)^^**`, `**^^Rampage^^**`.
- Nombres de habilidades citados entre comillas: `'Eruption of Fury'`,
  `'Power Through'`, `'Eat 'Em Alive'`.
- Habilidades de arma: `Crit (2 Hits)`, `Crit (Mortal)`, `Companion`,
  `Anti-Monster (+1 Rend)`, `Charge (+1 Damage)`, `Heal (D3)`.
- Nombres de características: `característica de Health`, `de Attacks`, `de Rend`.
- Nombres de unidades, armas, artefactos, trofeos y efectos, incluidos los que
  van en `***negrita cursiva***`: `***Squeezed Head***`, `***Steaming Brains***`.

Se traducen: todo lo demás, incluidos los términos de reglas que no son nombres
(`pile-in move`, `control score`, `fury level`, `damage points`…).

Una cadena que solo contiene palabras clave (`**^^Core^^**, **^^Move^^**`) se
deja con el valor vacío: no hay nada que traducir en ella.

## Glosario acordado

Para que dos personas traduciendo dos ficheros distintos no usen dos palabras
distintas. Amplíalo cuando aparezca un término nuevo.

| Inglés | Español |
| --- | --- |
| hit / wound / save / ward roll | tirada de impacto / de herida / de salvación / de salvaguardia |
| charge / casting / chanting / run roll | tirada de carga / de lanzamiento / de cántico / de correr |
| unmodified roll | tirada sin modificar |
| re-roll | volver a tirar |
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
- `<fichero>_es.cat` — el artefacto generado, para quien solo quiera descargarlo.

Antes de hacer commit, ejecuta `python tools/verify-translation.py`. Si no dice
`OK`, no lo subas.
