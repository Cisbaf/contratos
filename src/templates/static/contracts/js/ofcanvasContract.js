var myOffcanvas;
var ulGroup;
var objContract;
var numberContract;
var numberProcess;
var company;
var cnpjCpf;
var valueGlobal;
var valueMensal;
var startDate;
var endDate;
var font;
var inputPk;
var selectTa;
var method;


function CreateContractCanvas(){
    method.value = "POST";
    inputPk.value = '';
    numberContract.value = '';
    numberProcess.value = '';
    objContract.value = '';
    company.value = '';
    cnpjCpf.value = '';
    valueGlobal.value = '';
    valueMensal.value = '';
    startDate.value = '';
    endDate.value = '';
    font.value = '';
    const lis = ulGroup.querySelectorAll("li");
    lis.forEach(li=>{
        const input = li.querySelector("input");
        input.checked = false;
    });
    myOffcanvas.show();
}

function EditContractCanvas(contract_json){
    const lis = ulGroup.querySelectorAll("li");
    lis.forEach(li=>{
        const input = li.querySelector("input");
        input.checked = false;
    });
    method.value = "PUT";
    inputPk.value = contract_json.id;
    numberContract.value = contract_json.number_contract;
    numberProcess.value = contract_json.number_process;
    objContract.value = contract_json.object;
    company.value = contract_json.company;
    cnpjCpf.value = contract_json.cnpj_cpf;
    valueGlobal.value = contract_json.value_global;
    valueMensal.value = contract_json.value_mensal;
    startDate.value = contract_json.start_date;
    endDate.value = contract_json.end_date;
    font.value = contract_json.font;
    const fiscaisID = contract_json.fiscais.map((fiscal)=> String(fiscal.id) );
    lis.forEach(li=>{
        const input = li.querySelector("input");
        if(fiscaisID.includes(input.value)){
            input.checked = true;
        }
    })
    taOptions = selectTa.querySelectorAll('option');
    taOptions.forEach(option=>{
        if (option.value == contract_json.ta) option.selected = true;
    })
    myOffcanvas.show();
}

async function SetSelect(){
    const fiscais = await APIGetFiscais();
    fiscais.forEach((fiscal, i) => {
        const label = document.createElement("label");
        label.htmlFor = `input-${i}`;
        label.innerHTML = `${fiscal.name} (${fiscal.sector.name})`;
        const li = document.createElement("li");
        li.className = "list-group-item";
        const input = document.createElement("input");
        input.id = `input-${i}`
        input.className = "form-check-input me-1";
        input.type = "checkbox";
        input.name = "fiscais";
        input.value = fiscal.id;
        li.appendChild(input);
        li.appendChild(label);
        ulGroup.appendChild(li);
    });

}

async function SetSelectTas(tas_json){
    window.addEventListener("load", (e)=>{
        let option_default = document.createElement('option');
        option_default.value = "";
        option_default.innerText = "--";
        selectTa.appendChild(option_default);
        tas_json.forEach(ta=>{
            const option = document.createElement('option');
            option.value = ta[0];
            option.innerText = ta[1];
            selectTa.appendChild(option);
        })
    })
}

window.addEventListener('load', (e)=>{
    myOffcanvas = new bootstrap.Offcanvas(document.getElementById('canvasCreateContract'));
    method = document.getElementById("method");
    inputPk = document.getElementById("pk");
    ulGroup = document.getElementById("ulGroup");
    objContract = document.getElementById("objectContract");
    numberContract = document.getElementById("numberContract");
    numberProcess = document.getElementById("numberProcess");
    company = document.getElementById("company");
    cnpjCpf = document.getElementById("cnpjCpf");
    valueGlobal = document.getElementById("valueGlobal");
    valueMensal = document.getElementById("valueMensal");
    startDate = document.getElementById("startDate");
    endDate = document.getElementById("endDate");
    font = document.getElementById("font");
    selectTa = document.getElementById("selectTa");
    SetSelect();
})