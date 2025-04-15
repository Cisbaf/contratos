
function DeleteContract(number, pk){
    if(confirm(`Deseja realmente deletar o contrato ${number}?`) == true){
        window.location.href = '/contract/delete/' + pk;
    }
}
