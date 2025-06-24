# Reporte de Inspección Inicial - SonarCloud

## Quality Issue 1

- **Archivo:** `./ISW_2025-01/enterSources/forms.py`
- **Línea:** 4
- **Software Quality Impacted:** Maintainability
- **Tipo:** Code Smell
- **Severidad:** Low Impact (Bajo Impacto)
- **Descripción:** Class names should comply with a naming convention python:S101
- **Recomendación:** Rename class "Bulletin_request" to match the regular expression ^_?([A-Z_][a-zA-Z0-9]*|[a-z_][a-z0-9_]*)$.
- **Acción:** Las clases afectadas en el archivo forms.py se les cambiara en nombre a uno mas convencional en la siguiente iteración.

![Quality Issue 1](QualityIssue1.png)

## Quality Issue 2

- **Archivo:** `./ISW_2025-01/enterSources/templates/insert.html`
- **Línea:** 4
- **Software Quality Impacted:** Reliability
- **Tipo:** Bug
- **Severidad:** Medium Impact
- **Descripción:** "\<title>" should be present in all pages Web:PageWithoutTitleCheck
- **Recomendación:** Add a \<title> tag to this page.
- **Acción:** Corregir inmediatamente agregando un titulo apropiado.

![Quality Issue 2](QualityIssue2.png)

## Quality Issue 3

- **Archivo:** `./ISW_2025-01/enterSources/templates/index.html`
- **Línea:** 63
- **Software Quality Impacted:** Maintainability
- **Tipo:** Code Smell
- **Severidad:** Medium Impact
- **Descripción:** Prefer tag over ARIA role Web:S6819
- **Recomendación:** Use <img> instead of the img role to ensure accessibility across all devices.
- **Acción:** Corregir instanciando de manera correcta la imagen para asegurar la accesibilidad de la imagen.

![Quality Issue 3](QualityIssue3.png)
