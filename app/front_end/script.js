document.getElementById("contratanteForm").addEventListener("submit", async function (e) {
    e.preventDefault();

    const contratante = {
        cpf: document.getElementById("cpf").value,
        nome: document.getElementById("nome").value,
        idade: parseInt(document.getElementById("idade").value),
        genero: document.getElementById("genero").value === "true",
        email: document.getElementById("email").value,
        descricao: document.getElementById("descricao").value,
        quantidade: parseInt(document.getElementById("quantidade").value)
    };

    try {
        const response = await fetch("http://127.0.0.1:8000/api/contratante/", {
            method: "POST",
            headers: {
                "Content-Type": "application/json"
            },
            body: JSON.stringify(contratante)
        });

        if (!response.ok) {
            throw new Error("Erro ao cadastrar contratante");
        }

        alert("Contratante cadastrado com sucesso!");
        listarContratantes();  // Atualiza lista
    } catch (error) {
        alert(error.message);
    }
});

async function listarContratantes() {
    const lista = document.getElementById("contratanteList");
    lista.innerHTML = "";

    try {
        const response = await fetch("http://127.0.0.1:8000/api/contratantes/");
        const data = await response.json();

        data.forEach(c => {
            const item = document.createElement("li");
            item.textContent = `${c.nome} - ${c.email}`;
            lista.appendChild(item);
        });
    } catch (error) {
        console.error("Erro ao carregar contratantes:", error);
    }
}

// Chamada inicial para preencher a lista
listarContratantes();
