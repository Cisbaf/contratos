
function SearchByTable(inputID, rowSearch, columnFilter, key){
    const idsTr = {};
    const inputSearch = document.getElementById(inputID);
    if(!inputSearch) return;
    const value_filter = inputSearch.value;
    document.querySelectorAll(rowSearch).forEach(rowElement=>{
        if(rowElement.style.display == "none") rowElement.style.display="";
    })
    const elements = document.querySelectorAll(columnFilter);
    [...elements].map(element=>{
        const element_value = element.innerHTML;
        if(element_value.toLowerCase().includes(value_filter.toLowerCase())){
            const pk = element.getAttribute('data-pk');
            idsTr[pk] = `${key}-${pk}`
        }
    });
    const idsShow = Object.keys(idsTr).map(key=>idsTr[key]);
    document.querySelectorAll(rowSearch).forEach(rowElement=>{
        if(!idsShow.includes(rowElement.id)){
            rowElement.style.display = "none";
        }
    })
}