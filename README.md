# Age of Sigmar 4th — Spanish Translation

Unofficial Spanish translation of:
https://github.com/BSData/age-of-sigmar-4th

This project is not affiliated with or endorsed by Games Workshop,
BSData or New Recruit.

---

## Disclaimer / Aviso legal

**English.** This is an **UNOFFICIAL**, fan-made Spanish translation of the
[BSData/age-of-sigmar-4th][upstream] dataset. It is not affiliated with,
endorsed by, sponsored by or approved by Games Workshop, BSData or New Recruit.

- *Warhammer*, *Warhammer Age of Sigmar*, and all associated rules, profiles,
  names, characters, illustrations and imagery are either ® or ™, and/or © Games
  Workshop Limited. All rights in the original material remain with their
  respective owners. No challenge to their status is intended.
- The rules content in these files comes from the [BSData][upstream] community
  project and is reproduced here only to make a Spanish translation possible.
- This project is **free**. It carries no advertising, no donations, no
  sponsorship and no monetisation of any kind, and it is not distributed for
  commercial gain.
- It contains no Games Workshop logos, artwork or branding.
- The translation is **not official**. Games Workshop's own Spanish-language
  publications are always the authoritative terminology.
- If Games Workshop or BSData ask for this repository to be taken down, it will
  be taken down. Open an issue or contact the repository owner.

**Español.** Esto es una traducción al español **NO OFICIAL** y hecha por
afición del conjunto de datos [BSData/age-of-sigmar-4th][upstream]. No está
afiliada, respaldada, patrocinada ni aprobada por Games Workshop, BSData ni
New Recruit.

- *Warhammer*, *Warhammer Age of Sigmar* y todas las reglas, perfiles, nombres,
  personajes, ilustraciones e imágenes asociadas son ® o ™, y/o © Games Workshop
  Limited. Todos los derechos sobre el material original pertenecen a sus
  respectivos propietarios y no se pretende cuestionarlos.
- El contenido de reglas de estos ficheros proviene del proyecto comunitario
  [BSData][upstream] y se reproduce aquí solo para hacer posible la traducción.
- El proyecto es **gratuito**: sin publicidad, sin donaciones, sin patrocinios y
  sin monetización de ningún tipo. No se distribuye con ánimo de lucro.
- No incluye logotipos, ilustraciones ni imagen de marca de Games Workshop.
- La traducción **no es oficial**. La terminología correcta es siempre la de las
  publicaciones en español de Games Workshop.
- Si Games Workshop o BSData piden la retirada del repositorio, se retira. Abre
  un issue o contacta con el propietario del repositorio.

## Licencia

**Este repositorio no lleva licencia MIT, Apache ni similar, de forma
deliberada.** El material original no se publica bajo ninguna de esas
licencias, así que no se puede relicenciar aquí.

Lo único de cosecha propia son las herramientas de `tools/` y las traducciones
de `translations/`. Los ficheros `.cat`/`.gst` son obra derivada del
repositorio original y se comparten aquí en las mismas condiciones de
aficionado: uso personal, sin ánimo de lucro y con atribución.

*No license file is provided, deliberately: the source material is not
published under a permissive license, so it cannot be relicensed here.*

## Qué hay en este repositorio

| | |
| --- | --- |
| `*.cat`, `*.gst` | los ficheros originales en inglés, tal cual vienen de [BSData][upstream] |
| `*_es.cat` | la versión traducida al español |
| `translations/*.es.json` | el trabajo de traducción, cadena a cadena |
| `tools/` | las tres herramientas que generan los `_es.cat` |
| [`TRADUCIR.md`](TRADUCIR.md) | **cómo colaborar en la traducción** |

Estado actual: `Ogor Mawtribes.cat` traducido (54 de sus 58 cadenas
descriptivas; las otras 4 solo contienen palabras clave).

### La regla que no se puede saltar

Solo se traduce el contenido descriptivo: el texto dentro de `<description>` y
`<characteristic>`. **Los IDs no se traducen nunca**, ni `name=`, ni `type=`, ni
ningún otro atributo. `tools/verify-translation.py` lo comprueba byte a byte en
cada ejecución. Los detalles, en [`TRADUCIR.md`](TRADUCIR.md).

### Aviso sobre los `_es.cat`

Cada `_es.cat` conserva el `id` del catálogo original, porque los ids no se
traducen. Eso significa que **sustituye** al fichero original, no convive con
él: dos catálogos con el mismo id rompen el CI de BSData y New Recruit no debe
cargar los dos a la vez.

## Errores

- **Errores de traducción** (algo mal traducido o sin traducir): abre un issue
  en este repositorio.
- **Errores de datos** (puntos mal, un perfil incorrecto, una unidad que falta):
  son del proyecto original, repórtalos en [BSData/age-of-sigmar-4th][bug report].
  Cuando lo arreglen, llegará aquí al actualizar.

---

# Documentación original de BSData

*Lo que sigue es el README del repositorio original, conservado tal cual.*

## Overview ##

__How do I load this in Battlescribe?__

Battlescribe is abandonware and this dataset no longer supports it. If you really want, you can load it manually, but it will be extremely glitchy (e.g. reinforcing units does not double their points cost). Use New Recruit instead.

__I found a bug!__ / __I have another request__

Great, thank you! Please [Report a bug][bug report] - you can also suggest enhancements and raise other issues there. Make sure your issue has not already been reported.

__How do I create regiments in New Recruit?__ 

When you create a list, you will have a single parent force loaded with your general army composition options like lores and battle formation. to add a regiment (or auxiliary units), navigate to the sidebar and select the Regiments and Auxiliary category. You can add a child force there. Click your faction name and then Regiment or Auxiliary as needed (each regiment will need its own force). You can also add regiments of renown in this manner. To quickly navigate to unit entry for a specific regiment, click its header in the list view. That will scroll the sidebar panel to that regiment's selections where you can add units to it as needed.

## Links ##

* [Repositorio original / original repository][upstream]
* [BSData organization homepage][BSData.net]
* [New Recruit app homepage](https://www.newrecruit.eu/)

[upstream]: https://github.com/BSData/age-of-sigmar-4th
[BSData.net]: https://www.bsdata.net/
[bug report]: https://github.com/BSData/age-of-sigmar-4th/issues/new/choose
