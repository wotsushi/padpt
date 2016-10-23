# PadPT
PadPT generates a walkthrough sheet for Puzzle & Dragons from a text file.

## LICENSE
MIT

## Input
Input text files follow the below format.

    <title>

    <party>

    <party>

    <note>

Here,

    <title> ::= (<namechar>|,)*
    <party> ::= <member>{0,5}
    <member> ::= (<monster>|<monster>,<monster>)\n
    <monster> ::= <namechar>+
    <namechar> ::= <any character except \n or ,>
    <note> ::= <any string>


|Element                |Mean                                              |
|:----------------------|:-------------------------------------------------|
|Title                  |title (e.g., dungeon name)                        |
|The former party       |party A                                           |
|The later party        |party B                                           |
|Note                   |walkthrough                                       |
|Member                 |monster name and assist monster name if any       |

For example,

    ミル降臨

    覚醒劉備,覚醒ハーデス
    ディオス
    ディオス
    ディオス
    木アスタロト,光ラー

    覚醒劉備,タナトス
    ディオス
    ディオス
    ディオス
    木アスタロト,アヴァロン

    1F: Aディオス
    2F: Bアヴァロン
    3F: Aハーデス，ディオス
    4F: Bディオス
    5F: Aラー
    6F: Aディオス
    7F: Bディオス
    8F: A0コンボ，Bタナトス，A0コンボ，B0コンボ，A0コンボ，Bディオス

## Output
Output files are png format.
Output files have the following information:
* Title
* Timestamp (automatically)
* Monster icons of party A
* Monster icons of party B
* The numbers of awoken skills
 * Skill boost
 * Resistance-skill lock
 * Resistance-jammers
 * Resistance-poison
 * Resistance-dark
* Note/Walkthrough

For example, PadPT outputs the following sheet from the input example:

![out](./docs/example.png)

## Dependencies
* Python 3.5.2
* Pillow 3.3.0

## Config
Edit config files in ~/.padpt/ before using PadPT.
The config files are following:
* alias.csv
* padpt.conf

Note: the config files must be encoded in UTF-8.

### alias.csv
Configure monster name alias by editing ~/.padpt/alias.csv.
Records in the csv follow the below format:

    <monster>,<natural number>

For example,

    覚醒劉備,2903
    ディオス,2948
    タナトス,923

Note that there must not exist two or more than records
that have the same monster name (the first element).
The natural number (the second element) is the monster number.
The number must be consistent with database.

### padpt.conf
Configure font used in output sheets, database URL for update
by editing ~/.padpt/padpt.conf.
The conf file follows the below format:

    [PadPT]
    Font=<path>
    DB_URL=<URL>

DB_URL must satisfy the following two conditions:

* *DB_URL*/monsters.csv is a csv file
* For any recored in *DB_URL*/monsters.csv, let *i* be the first element.
Then, *DB_URL*/icons/*i*.jpg is a jpg file

Records in *DB_URL*/monsters.csv follows the below format:

    monster_id,skill_boost,skill_lock,jammers,poison,dark
    <natural number that may be suppressed 0>,<non-negative integer>{5,5}

An example of conf/padpt.conf is shown below,

    [PadPT]
    Font=/System/Library/Fonts/ヒラギノ角ゴ ProN W6.otf
    DB_URL=http://www.foo.jp/padpt

## Script Usage
### Output a Sheet
Let x be an input text file and y be an output png file. Then,

    padpt x y

### Update Database

    padpt -u

You can specify the update option, an input file,
and an output file at the same time.
So the following command is valid where x is an input text file and
y be an output png file.

    padpt -u x y

## Note
PadPT has no connections with Puzzle & Dragons and GungHo Online Entertainment.
