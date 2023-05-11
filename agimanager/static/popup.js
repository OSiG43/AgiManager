const shadowBack = document.getElementById("shadowBack");
const addCmdPopup = document.getElementById("addCmdPopup");

addCmdPopup.querySelector('#cancelBtn').addEventListener("click", ()=>{
    closeAddCmdPopup();
});

addCmdPopup.querySelector('#kit-1').addEventListener("change", addCmdKitChangeListener);


function addCmdKitChangeListener(event){

    if(event.target.value !== "-1"){
         let template = addCmdPopup.querySelector("#form-group-template");
        let liste_cmd_kit = addCmdPopup.querySelector("#list-cmd-kit");

        //On créer le nouvelle élement.
        let node = document.createElement("div");
        node.innerHTML = interpolate(template.innerHTML, {index:Date.now()});//On utilse Date.now() de manière a avoir un id unique

        liste_cmd_kit.appendChild(node);

        event.target.removeEventListener("change", addCmdKitChangeListener);

        //si on repasse une ligne kit à l'option par défaut --> alors on supprime la ligne de choix de kit
        event.target.addEventListener("change", ()=>{
            if(event.target.value === "-1"){
                event.target.parentElement.parentElement.remove();
            }
        });

        node.querySelector("select").addEventListener("change", addCmdKitChangeListener);
    }
}


function openAddCmdPopup(){
    //on affiche le voile noir et la popup
    addCmdPopup.style.display="block";
    shadowBack.style.display = "block";
}

function closeAddCmdPopup(){
    addCmdPopup.style.display="none";
    shadowBack.style.display = "none";
}