var myOffcanvas;
var inputNameCanvas;
var inputEmail;
var inputTel;
var inputSector;
var inputPassword;
var divPass;
var inputPk;
var method;

function parseJsonWithSingleQuotes(jsonString) {
    const jsonStringDoubleQuoted = jsonString.replace(/(['"])?([a-zA-Z0-9_]+)(['"])?:/g, '"$2":').replace(/'/g, '"');
    const parsedObject = JSON.parse(jsonStringDoubleQuoted);
    return parsedObject;
}

async function SetSelect(){
  const sectors = await APIGetSectores();
  if(!sectors) return;
  const select = document.getElementById("sectorFiscal");
  if(!select) return;
  sectors.forEach(sector=>{
    const option = document.createElement('option');
    option.value = sector.id;
    option.innerHTML = sector.name;
    select.appendChild(option);
  })
}

function CreateUserCanvas(){
    method.value = "POST";
    inputNameCanvas.value = '';
    inputEmail.value = '';
    inputTel.value = '';
    divPass.style.display = "block";
    myOffcanvas.show();
}

function EditUserCanvas(user_json_str){
    const user_json = parseJsonWithSingleQuotes(user_json_str);
    method.value = "PUT";
    inputPk.value = user_json.id;
    inputNameCanvas.value = user_json.name;
    inputEmail.value = user_json.email;
    inputTel.value = user_json.cell_phone;
    divPass.style.display = "none";
    for (var i = 0; i < inputSector.options.length; i++) {
        console.log(inputSector.options[i].value, user_json.sector.id);
        if (inputSector.options[i].value === `${user_json.sector.id}`) {
            inputSector.selectedIndex = i;
            break;
        }
    }
    myOffcanvas.show();
}

window.addEventListener('load', (e)=>{
  myOffcanvas = new bootstrap.Offcanvas(document.getElementById('canvasCreateUser'));
  method = document.getElementById("method");
  inputPk = document.getElementById("pk");
  inputNameCanvas = document.getElementById("nameFiscal");
  inputEmail = document.getElementById("emailFiscal");
  inputTel = document.getElementById("telFiscal");
  inputSector = document.getElementById("sectorFiscal");
  inputPassword = document.getElementById("passwordFiscal");
  divPass = document.getElementById("divPass");

  SetSelect();
})