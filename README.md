# KingsChat Login Actions — Python

Automatización de sesiones y acciones en [KingsChat](https://web.kingsch.at/) usando **Python + Selenium + Firefox**.

El script lee una lista de cuentas, inicia sesión en cada una y realiza acciones configurables: **publicar un estado**, **dar like**, **compartir** y **comentar** un post.

## ¿Qué hace?

Para cada cuenta en `Names.csv`:

1. Abre `https://web.kingsch.at/` y hace login.
2. Publica un estado aleatorio desde `Status.txt`.
3. Abre el post indicado en `Post.txt`.
4. Opcionalmente: hace **like**, **share** y/o **comment** (comentario aleatorio de `Comentarios.txt`).
5. Limpia cookies y pasa a la siguiente cuenta.

## Archivos

| Archivo | Descripción |
|---|---|
| `navegador.py` | Script principal (Selenium / Firefox). |
| `Names.csv` | Lista de cuentas, una por línea: `usuario,contraseña`. |
| `Post.txt` | URL del post sobre el que se actúa. |
| `Status.txt` | Estados posibles (se elige uno al azar). |
| `Comentarios.txt` | Comentarios posibles (se elige uno al azar). |
| `geckodriver.exe` | Driver de Firefox para Windows. |

## Configuración

En `navegador.py` se activan/desactivan las acciones con estas banderas:

```python
oLike    = "OFF"   # Like al post       (ON / OFF)
oShare   = "OFF"   # Compartir el post  (ON / OFF)
oComment = "OFF"   # Comentar el post   (ON / OFF)
```

## Requisitos

- Python con `selenium` (`pip install selenium`).
- Mozilla Firefox instalado.
- `geckodriver` en el `PATH` (incluido para Windows).

## Uso

```bash
# 1. Coloca las cuentas en Names.csv (una por línea: usuario,contraseña)
# 2. Ajusta las banderas en navegador.py
# 3. Ajusta Post.txt, Status.txt y Comentarios.txt
python navegador.py
```

## Notas

- El código fue escrito para **Python 2** y una versión antigua de Selenium (usa `find_element_by_xpath`, `firefox_profile` y `print e`). Para ejecutarlo hoy hay que actualizarlo a Python 3 y Selenium 4.
- Los localizadores (XPath) apuntan a la estructura del sitio web y pueden cambiar.
- Úsalo únicamente con cuentas propias y respetando los términos de servicio de la plataforma.
