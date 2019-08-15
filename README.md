# scorpion
🦂 Secure Copy Protocol (scp) script to automate transfer process

Named after `scp` (Security Copy Protocol) bash command as **sc**or**p**ion, automate the sharing process using a config file.

Scorpion is a script that runs `ssh` and `scp` in order to accomplish the following tasks:

1. Delete existing `target` directory.
2. Create the previously removed directory.
3. Copy contents from `origin` directory to `target` directory.

`target` directory and `origin` directory are paths specified in a json file called `scorpion.json`.

The script logs every command and asks for `sudo` before executing it.
The following is a sample of the commands `scorpion` runs in order to accomplish its tasks.

```bash
[SCORPION]      ::      Running $ ssh admin@0.0.0.0 rmdir /www/website.com/
# (asks for sudo)
[SCORPION]      ::      Running $ ssh admin@0.0.0.0 mkdir -p /www/website.com/
# (asks for sudo)
[SCORPION]      ::      Running $ scp -r ./dist/* admin@0.0.0.0:/www/website.com/
# (asks for sudo)
```

## Requirements
- Python 3.7

## Installation
To download `scorpion.py` script, run **cURL** from your project directory as follows:

```bash
curl -L https://raw.githubusercontent.com/estebanborai/scp-scorpion/master/scorpion/scorpion.py >> scorpion.py
```

## Usage
Run scorpion from you project root directory as follows:
```bash
python ./scorpion.py
```

In order to run `scorpion`, a config file should be available in the context of the process.
The following is an example of a `scorpion.json`.
```javascript
{
  "user": "admin", // The address user
  "address": "0.0.0.0", // The address to copy files (IP)
  "origin": "./dist/*", // The files to copy
  "target": "/www/website.com/" // The target path of the files
}
```
If the `scorpion.json` file is not available, the user will be prompted in order to generate a new configuration file.
