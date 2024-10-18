

async function APIGetFiscais(){
    const response = await fetch('/accounts/get_users');
    return await response.json();
}

async function APIGetSectores(){
    const response = await fetch('/contract/sector/all');
    return await response.json();
}