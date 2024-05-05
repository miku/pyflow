# Code Quality

## Assess how much code it there in the first place

* tokei

```
===============================================================================
 Language            Files        Lines         Code     Comments       Blanks
===============================================================================
 Autoconf                1            7            6            0            1
 CSS                    11          322          241           29           52
 INI                     1          145          129            8            8
 JavaScript             17         5871         5043          285          543
 Makefile                1          177          143            6           28
 Python                254        61008        45068         5111        10829
 ReStructuredText       15         3165         2323            0          842
 Shell                   4          104           83            6           15
 SVG                     2          794          794            0            0
 TOML                    3           64           46            7           11
 XML                     1            9            8            0            1
 YAML                    2           45           37            3            5
-------------------------------------------------------------------------------
 HTML                    7          457          401           19           37
 |- CSS                  2           76           54           11           11
 |- JavaScript           2          415          404            5            6
 (Total)                            948          859           35           54
===============================================================================
 Total                 319        72168        54322         5474        12372
===============================================================================
```

## Linting and Code checks

* pylint

```
$ pylint --list-msgs
```

Includes security issues like `forgotten-debug-statement` and the like.

Another (meta) static code analysis tool is prospector.

```
$ pip install prospector[with_mypy,with_bandit]
```

Or just with everything:

```
$ pip install prospector[with_everything]
```

Example running against a Python OSS project with about 60K SLOC ([spotify/luigi](repo)):

```
$ prospector

...

Check Information
=================
         Started: 2022-09-06 20:37:04.522971
        Finished: 2022-09-06 20:37:49.662702
      Time Taken: 45.14 seconds
       Formatter: grouped
        Profiles: default, no_doc_warnings, no_test_warnings, strictness_medium, strictness_high, strictness_veryhigh, no_member_warnings
      Strictness: None
  Libraries Used: 
       Tools Run: dodgy, mccabe, profile-validator, pycodestyle, pyflakes, pylint
  Messages Found: 1399
```

It comes with a set of profiles:

* [https://github.com/PyCQA/prospector/tree/master/prospector/profiles/profiles](https://github.com/PyCQA/prospector/tree/master/prospector/profiles/profiles)

For example a [strictness_veryhigh](https://github.com/PyCQA/prospector/blob/master/prospector/profiles/profiles/strictness_veryhigh.yaml)

```
# This will enable almost every single warning
allow-shorthand: false

ignore-patterns:
  - (^|/)\..+

pylint:
  disable:
    - fixme
    - bad-continuation

  options:
    max-locals: 15
    max-returns: 6
    max-branches: 12
    max-statements: 50
    max-parents: 7
    max-attributes: 7
    min-public-methods: 2
    max-public-methods: 20
    max-module-lines: 1000
    max-line-length: 79

mccabe:
  options:
    max-complexity: 10

pycodestyle:
  options:
    max-line-length: 79
    single-line-if-stmt: n

pyroma:
  disable:
    - PYR19
    - PYR16

pydocstyle:
  disable:
    - D000
```


## Security Audit: bandit

> Bandit is a tool designed to find common security issues in Python code. To do
> this, Bandit processes each file, builds an AST from it, and runs appropriate
> plugins against the AST nodes. 

```
$ bandit -r luigi

...

Code scanned:
        Total lines of code: 21186
        Total lines skipped (#nosec): 0

Run metrics:
        Total issues (by severity):
                Undefined: 0
                Low: 122
                Medium: 34
                High: 7
        Total issues (by confidence):
                Undefined: 0
                Low: 7
                Medium: 9
                High: 147
Files skipped (0):
```

Plugins (e.g. [pickle](https://docs.python.org/3/library/pickle.html)).

```
The following tests were discovered and loaded:
-----------------------------------------------
        B101    assert_used
        B102    exec_used
        B103    set_bad_file_permissions
        B104    hardcoded_bind_all_interfaces
        B105    hardcoded_password_string
        B106    hardcoded_password_funcarg
        B107    hardcoded_password_default
        B108    hardcoded_tmp_directory
        B110    try_except_pass
        B112    try_except_continue
        B201    flask_debug_true
        B301    pickle
        B302    marshal
        B303    md5
        B304    ciphers
        B305    cipher_modes
        B306    mktemp_q
        B307    eval
        B308    mark_safe
        B309    httpsconnection
        B310    urllib_urlopen
        B311    random
        B312    telnetlib
        B313    xml_bad_cElementTree
        B314    xml_bad_ElementTree
        B315    xml_bad_expatreader
        B316    xml_bad_expatbuilder
        B317    xml_bad_sax
        B318    xml_bad_minidom
        B319    xml_bad_pulldom
        B320    xml_bad_etree
        B321    ftplib
        B323    unverified_context
        B324    hashlib_insecure_functions
        B325    tempnam
        B401    import_telnetlib
        B402    import_ftplib
        B403    import_pickle
        B404    import_subprocess
        B405    import_xml_etree
        B406    import_xml_sax
        B407    import_xml_expat
        B408    import_xml_minidom
        B409    import_xml_pulldom
        B410    import_lxml
        B411    import_xmlrpclib
        B412    import_httpoxy
        B413    import_pycrypto
        B415    import_pyghmi
        B501    request_with_no_cert_validation
        B502    ssl_with_bad_version
        B503    ssl_with_bad_defaults
        B504    ssl_with_no_version
        B505    weak_cryptographic_key
        B506    yaml_load
        B507    ssh_no_host_key_verification
        B508    snmp_insecure_version
        B509    snmp_weak_cryptography
        B601    paramiko_calls
        B602    subprocess_popen_with_shell_equals_true
        B603    subprocess_without_shell_equals_true
        B604    any_other_function_with_shell_equals_true
        B605    start_process_with_a_shell
        B606    start_process_with_no_shell
        B607    start_process_with_partial_path
        B608    hardcoded_sql_expressions
        B609    linux_commands_wildcard_injection
        B610    django_extra_used
        B611    django_rawsql_used
        B701    jinja2_autoescape_false
        B702    use_of_mako_templates
        B703    django_mark_safe
```

Filter for high severity issues only:

```
$ bandit -r luigi --severity high -iii

...

--------------------------------------------------
>> Issue: [B605:start_process_with_a_shell] Starting a process with a shell, possible injection detected, security issue.
   Severity: High   Confidence: High
   CWE: CWE-78 (https://cwe.mitre.org/data/definitions/78.html)
   Location: luigi/lock.py:39:13
   More Info: https://bandit.readthedocs.io/en/1.7.4/plugins/b605_start_process_with_a_shell.html
38              cmd = 'wmic path win32_process where ProcessID=%s get Commandline 2> nul' % (pid, )
39              with os.popen(cmd, 'r') as p:
40                  lines = [line for line in p.readlines() if line.strip("\r\n ") != ""]

--------------------------------------------------
>> Issue: [B103:set_bad_file_permissions] Chmod setting a permissive mask 0o777 on file (pid_dir).
   Severity: High   Confidence: High
   CWE: CWE-732 (https://cwe.mitre.org/data/definitions/732.html)
   Location: luigi/lock.py:103:8
   More Info: https://bandit.readthedocs.io/en/1.7.4/plugins/b103_set_bad_file_permissions.html
102             os.mkdir(pid_dir)
103             os.chmod(pid_dir, 0o777)
104         except OSError as exc:

--------------------------------------------------

Code scanned:
        Total lines of code: 21186
        Total lines skipped (#nosec): 0

Run metrics:
        Total issues (by severity):
                Undefined: 0
                Low: 122
                Medium: 34
                High: 7
        Total issues (by confidence):
                Undefined: 0
                Low: 7
                Medium: 9
                High: 147
Files skipped (0):
```

## Commit hooks

* use commit hooks to run one or more style or auditing tools
* balance between warnings and actionable advice