class CommandInterface {
    constructor() {
        if (new.target === CommandInterface) {
            throw new TypeError("Cannot construct Abstract instances directly");
        }
    }

    async execute() {
        throw new Error("Not implemented");
    }
}

class Command extends CommandInterface {
    constructor({ url, body, headers, method }) {
        super();
        this.url = url;
        this.body = body;
        this.method = method.toUpperCase();
        this.headers = headers || {};
        if (!this.headers['Content-Type']) {
            this.headers['Content-Type'] = "application/json";
        }
    }

    async execute() {
        let config = {
            method: this.method,
            headers: this.headers,
        };

        if (this.method !== 'GET') {
            config.body = typeof this.body === 'string' ?
                this.body :
                JSON.stringify(this.body);
        }

        return await fetch(this.url, config);
    }
}

class Invoker {
    constructor() {
        this.command = null;
    }

    setCommand(command) {
        this.command = command;
    }

    validate() {
        console.log('Realizando validações...');
        if (!this.command) {
            throw new Error('Necessário configurar comando');
        }
        return true;
    }

    async send({renderOn}) {
        const resultInput = document.querySelector(renderOn);

        if (this.validate()) {
            let result = await this.command.execute();
            let resultText = await result.text();
            try {
                let resultJson = JSON.parse(resultText);
                resultInput.value = JSON.stringify(resultJson, null, 2);
            } catch (e) {
                resultInput.value = resultText;
            }
        }
    }
}

const main = async () => {
    const urlInput = document.getElementById('url');
    const bodyInput = document.getElementById('body');
    const methodInput = document.getElementById('method');

    let command = new Command({
        url: urlInput.value,
        body: bodyInput.value,
        method: methodInput.value
    });

    let invoker = new Invoker();
    invoker.setCommand(command);

    await invoker.send({renderOn: '#result'});
}