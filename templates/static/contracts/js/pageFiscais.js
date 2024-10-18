
function DeleteFiscal(name, pk){
    if(confirm(`Deseja realmente deletar ${name}?`) == true){
        window.location.href = '/accounts/delete/' + pk;
    }
}
