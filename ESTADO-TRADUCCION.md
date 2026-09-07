# Estado de la traducción — 7 de septiembre de 2026

Repositorio: `C:\dev\age-of-sigmar-4th-es`.

**La traducción completa del repositorio sigue pendiente.**

## Trabajo guardado

- Revisadas las instrucciones de `TRADUCIR.md`, el glosario, las herramientas y las traducciones existentes. Se mantiene la edición de JSON y la generación de XML sin alterar atributos ni identificadores.
- Añadidas 1.903 traducciones a entradas anteriormente vacías. Incluye reutilización de traducciones existentes, adaptación de fórmulas repetidas revisadas y traducción manual de reglas.
- Completada la prosa pendiente de las bibliotecas de **Blades of Khorne, Kharadron Overlords, Sylvaneth y Nighthaunt**. Sus entradas vacías restantes son palabras clave, nombres de habilidades de arma y datos de peanas que se conservan en inglés.
- Recuperado `translations/Age of Sigmar 4.0.es.json` desde el `.gst` español existente: 124 cadenas. No se ha retraducido ese contenido.
- Generadas y verificadas 133 parejas `.cat`/`.gst`. Se ha comprobado la estructura XML, todos los atributos y que cada texto generado corresponda a su JSON.
- Los originales ingleses permanecen intactos. No se ha hecho commit ni publicación.

## Pendiente

El siguiente recuento incluye exclusivamente entradas vacías de más de 90 caracteres: **no es un porcentaje de cobertura** y puede excluir etiquetas cortas todavía pendientes. Quedan 2.725 entradas largas en 17 archivos.

| Archivo | Entradas largas pendientes |
| --- | ---: |
| Cities of Sigmar - Library.cat | 198 |
| Daughters of Khaine - Library.cat | 94 |
| Disciples of Tzeentch - Library.cat | 105 |
| Flesh-eater Courts - Library.cat | 111 |
| Gloomspite Gitz - Library.cat | 113 |
| Hedonites of Slaanesh - Library.cat | 114 |
| Lores.cat | 665 |
| Lumineth Realm-lords - Library.cat | 113 |
| Maggotkin of Nurgle - Library.cat | 116 |
| Ossiarch Bonereapers - Library.cat | 96 |
| Path to Glory - Blighted Wilds.cat | 126 |
| Path to Glory - Ravaged Coast.cat | 102 |
| Regiments of Renown.cat | 211 |
| Skaven - Library.cat | 133 |
| Slaves to Darkness - Library.cat | 129 |
| Soulblight Gravelords - Library.cat | 132 |
| Stormcast Eternals - Library.cat | 167 |

## Continuación

Mantener el glosario y las reglas de `TRADUCIR.md`: conservar nombres, palabras clave, habilidades citadas y características en inglés; traducir la prosa. Rellenar las entradas vacías de los JSON y regenerar el catálogo correspondiente con `tools/apply-translation.py`. Ejecutar `tools/verify-translation.py` tras los cambios.

La verificación técnica no certifica la completitud lingüística. Los catálogos de los 17 archivos pendientes contienen todavía texto inglés. Se ha solicitado preferencia entre continuar manualmente por facción o utilizar traducción automática externa con revisión posterior; no se han enviado las reglas a un traductor externo.
