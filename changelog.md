# Changelog
### `v-1.2-0`
This is a final version until framework change or something unexpected happens.
1. Database now has a public variable: tables - list of every table in database.
(Useful to handle errors if table was not found to prevent crashes)
2. Table object now has a columns variable which is also a list. Obviously, it contains list of 
columns to get.
3. Two previous variables work for postgresql as stable and Use-At-Own-Risk in sqlite.
4. Code has been cleaned.
5. User class has been added if you want to quickly open multiple connections.


### `v1.1.0-a`

1. Removed readthedocs.org as I exhausted of writing this in rts and convertors from md to rst are bad.
2. On my way to add column/table recognition as it'll become the foundation of 2.0.0 update.
3. Code refactoring and quality
4. v1.1.0-b will be a testing version. No new changes will be made.

### `v1.0.0-r`

1. Docs adaptation for readthedocs.io
2. Some fixes
3. Added new features
4. I\'m bored with typing - check commit! **[[ab8532b]](https://github.com/SOLIDusr/requesto-py/commit/ab8532bb9c4a0ed883dcab75b7459e788634c4a1)**


### `v1.0.0-b`

1. Added changelog
2. Removed unused imports. **[[e87c34f]](https://github.com/SOLIDusr/requesto-py/commit/e87c34feec0d97c900b6f7eb91bec1b2381f98d6)**
3. Added README.md **[[f12449c]](https://github.com/SOLIDusr/requesto-py/commit/f12449cfca324f22c45d170b102ddf0e27e0a4b8)**
4. Added LICENSE
5. Added Table, Connection classes
6. Added methods to create a database object
7. Added sqlite3 support
8. Added methods to insert, update, select etc.
9. Fixed a ton of bugs **[[ef2f39a]](https://github.com/SOLIDusr/requesto-py/commit/ef2f39ac291e05aad86634fb46d52c60656fd533)**
**[[2e6857a]](https://github.com/SOLIDusr/requesto-py/commit/2e6857a85f3c778b7e63ef3c2cf6829e79e83a59)**

5 - 10 **[[30fd93f]](https://github.com/SOLIDusr/requesto-py/commit/30fd93fc4985041cc1be0b60f940368a8edf566c)**
