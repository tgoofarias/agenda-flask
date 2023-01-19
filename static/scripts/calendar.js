document.addEventListener("DOMContentLoaded", () => {
    const months = ["janeiro", "fevereiro", "março", "abril", "maio", "junho", "julho", "agosto", "setembro", "outubro", "novembro", "dezembro"];
    const tableDays = document.getElementById("dias");
    const getDaysCalendar = (mes, ano) => {
        document.getElementById("mes").innerHTML = months[mes];
        document.getElementById("ano").innerHTML = ano;

        let firstDayOfWeek = new Date(ano, mes, 1).getDay() - 1;
        let lastDayThisMonth = new Date(ano, mes + 1, 0).getDate();

        for (var i = -firstDayOfWeek, index = 0; i < (42 - firstDayOfWeek); i++, index++) {
            let dt = new Date(ano, mes, i);
            let dayTable = tableDays.getElementsByTagName("button")[index];
            dayTable.classList.remove("mes-anterior");
            dayTable.classList.remove("proximo-mes");
            dayTable.innerHTML = dt.getDate();

            if (i < 1) {
                dayTable.classList.add("mes-anterior");
            }
            else if ( i > lastDayThisMonth) {
                dayTable.classList.add("proximo-mes");
            }
        }
    }

    let now = new Date();
    let mes = now.getMonth();
    let ano = now.getFullYear();

    getDaysCalendar(mes, ano);

    const botao_anterior = document.getElementById("bnt_prev");
    const botao_proximo = document.getElementById("bnt_next");

    botao_proximo.onclick = () => {
        mes++;
        if (mes > 11) {
            mes = 0;
            ano++;
        }
        getDaysCalendar(mes, ano);
    }

    botao_anterior.onclick = () => {
        mes--;
        if (mes < 0) {
            mes = 11;
            ano--;
        }
        getDaysCalendar(mes, ano);
    }
})