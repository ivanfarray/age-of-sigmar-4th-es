# Estado de la traducción — 7 de septiembre de 2026

**La traducción completa del repositorio sigue pendiente.**

## Trabajo guardado

- Se mantiene el método de `TRADUCIR.md`: traducción de valores JSON y generación de XML sin modificar atributos, identificadores ni originales ingleses.
- El commit anterior `1fca7f4` añadió 1.903 traducciones y completó la prosa de Blades of Khorne, Kharadron Overlords, Sylvaneth y Nighthaunt. También recuperó 124 cadenas del JSON de reglas generales desde su versión española existente.
- Este bloque añade otras **2.619 traducciones** a entradas anteriormente vacías, con traducción manual y reutilización de textos revisados coincidentes.
- Completada la prosa pendiente de **Daughters of Khaine, Disciples of Tzeentch, Flesh-eater Courts, Gloomspite Gitz, Hedonites of Slaanesh, Lumineth Realm-lords, Maggotkin of Nurgle, Ossiarch Bonereapers, Skaven y Slaves to Darkness**, además de **Lores, Path to Glory - Blighted Wilds y Path to Glory - Ravaged Coast**.
- Las entradas vacías de esos archivos son palabras clave, habilidades de arma, medidas de peanas, dados y nombres de ingredientes con cantidades que se conservan en inglés.
- También se han reutilizado traducciones coincidentes en los cuatro archivos que siguen pendientes.
- Verificadas las 133 parejas `.cat`/`.gst`: estructura XML y atributos conservados. Los catálogos modificados se han comprobado además contra sus JSON al generarlos.
- Revisadas las cifras de las 2.619 traducciones nuevas. La única diferencia es la eliminación de una frase duplicada sobre el valor 6 en Disciples of Tzeentch; se conserva su regla. No se detectaron caracteres de sustitución ni signos de interrogación incrustados en palabras.
- Trabajo guardado localmente, sin publicación ni push.

## Pendiente

El siguiente recuento incluye exclusivamente entradas vacías de más de 90 caracteres: **no es un porcentaje de cobertura** y puede excluir etiquetas cortas todavía pendientes. Quedan **690 entradas largas en 4 archivos**.

| Archivo | Entradas largas pendientes |
| --- | ---: |
| Cities of Sigmar - Library.cat | 193 |
| Regiments of Renown.cat | 205 |
| Soulblight Gravelords - Library.cat | 128 |
| Stormcast Eternals - Library.cat | 164 |

## Continuación

Completar los cuatro archivos pendientes siguiendo el glosario y las reglas de `TRADUCIR.md`: conservar nombres, palabras clave, habilidades citadas y características en inglés; traducir la prosa. Rellenar los valores vacíos de los JSON, regenerar con `tools/apply-translation.py` y ejecutar `tools/verify-translation.py`.

La verificación técnica no certifica la completitud lingüística. Estos cuatro catálogos contienen todavía prosa inglesa. No se han enviado las reglas a un traductor externo.
