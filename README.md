# [SourceCodeLicenser-Python](http://www.etrotech.com)

- its a source file header management utility base on [Spairaru framework](http://www.spairaru.com).
- developed for internal use originally, free for public use.
- collaboration or service request, contact [me](https://github.com/micah0912).
- a coffee donation will help to keep the package updated :)

\
<tab>

### Highlights
---

- With custom files stored in `.scl` folder in each directory, settings can be overridden and stacked up.
- As the result, you can apply different header template with dynamitic text to all or specified file accordingly.
- Easy switch to license and un-license files for development or release branch, development or production state, by the use of your scenario.
- Auto generate `LICENSE.txt` with default or customized template, and with dynamic text.

\
<tab>

### Supporting File Types
---

Currently supported source file types are below, will continue to expand in future release.

- **.cnf**, **.css**, **.cmd**, **.html**, **.ini**, **.java**, **js**, **.php**, **.py**, **.sh**, **.swift**, **.ts**, **.xml**

\
<tab>

### Environment Requirements
---

1. Python version 3.9+

\
<tab>

### Dependency Requirements
---

1. Spairaru-Python framework
	 - information and documentation, see [Git](https://github.com/etrotech/Spairaru-Python) or [Web](http://www.spairaru.com).

```python    
    # importing spairaru must be fesible

    import sprr
```

\
<tab>

### Installation
---

1. **PIP**
 
	- To be determine.

```python    
    # TBD

    $ pip install xxxxxxxxx
```

\
<tab>

2. **Installer**
	1. Download from [Git](https://github.com/etrotech/SourceCodeLicenser) or [Web](http://www.etrotech.com).
	2. Extra and find installer in `__installation__` folder.
	3. Execute installer.

\
<tab>

3. **Manually**
	1. Download from [Git](https://github.com/etrotech/SourceCodeLicenser) or [Web](http://www.etrotech.com).
	2. Extra and move `src` source folder or `dist` distribution folder to python path or working directory.
	3. rename `src` or `dist` folder to preferred name; Suggest to `scl`.

\
<tab>  

### Basic Usage
---

**To apply license**

```python
# long syntax
from scl import SourceCodeLicenser

SourceCodeLicenser.license( "__path_of_application_root__" )


# short syntax
from scl import scl

scl.lic( "__path_of_application_root__" )
```

\
<tab>

**To dispose license**

```python
# long syntax
from scl import SourceCodeLicenser

SourceCodeLicenser.unlicense( "__path_of_application_root__" )


# short syntax
from scl import scl

scl.ulic( "__path_of_application_root__" )
```

\
<tab>  

### Advanced Usage
---

**copy to and license in different folder**

```python
# give `dist` or `distribution` option

scl.lic(
	"__path_of_application_root__" 
	# Locational Options
	# distribution_directory
	, dist = "__path_of_distribution_root__" 
)
```

**license over symbolic folders and files**

```python
# give `flw_lnk` or `flow_link` option

scl.lic(
	"__path_of_application_root__" 
	# Search Options
	# follow_link
	, flw_lnk = True
)
```
\
<tab>

### Customization
---

- place add custom `.tpl` template files or `.cnf` configuration files, or `.ign` ignore glob patterns in `.scl` folder.

```
# Exanple Hierarchy

__path_of_application_root__

    + .scl
        - custom.tpl
        - custom.ign
        - custom.cnf
    + __some_folder__
    + __some_folder__
        + .scl
            - custom.tpl
            - custom.ign
            - custom.cnf
```

- If no `.tpl` present, settings will inherit from parent directory.

\
<tab>


### Custom - Template
---

**Naming**

- For default template, name it to `@.tpl`.
- To specify template, name it to `__name__.__extention__.tpl`.

```
# Exanple Naming

__path_of_application_root__

    + .scl
        - @.tpl
    + __some_folder__
        + .scl
            - test.html.tpl
        - test.html
```

- In above hierarchy,
	- `test.html` will apply to `test.html.tpl`.
	- the rest of file will apply `@.tpl`

\
<tab>

**Design**

- Input text <u>without comment</u> in template file.
- Where the dynamic variable surround it with double braces plus parent mark.
- Dynamic variables can define in `.cnf` configuration files.

```
# Exanple of xxx.tpl

{{%SCL_PTN_NM}} {{%SCL_PTN_VER}}

Copyright {{%SCL_LIC_HLDR}} {{%SCL_LIC_YR}}. All Rights Reserved.

This file is part of {{%SCL_PTN_NM}}, which released under {{%SCL_LIC_TYP}}.
```

```
# above example in licensing stage outputs below

SourceCodeLicenser-Python sr1.0.0

Copyright EtroTech, and its contributor 2022. All Rights Reserved.

This file is part of SourceCodeLicenser, which released under GPL-3.0-or-later.
```

\
<tab>

### Custom - Configuration
---

- `.cnf` configuration file use standard `.conf` or `.ini` file syntax.
- Configuration category must be `[scl]`

```
# Exanple of xxx.cnf

[scl]
__custom_var_Name__=__Custom_Var_Value__
```

\
<tab>

### Custom - Ignores
---

- By adding glob pattern to `.ign` ignore file be faster license or un-license processes.
- Accept standard glob syntax.

```
# Exanple of xxx.ign

**/**.__extension__
**/__folder_name__
```