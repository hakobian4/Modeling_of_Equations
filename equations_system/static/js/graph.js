var elt = document.getElementById('calculator');
var calculator = Desmos.GraphingCalculator(elt);
var a = document.getElementById("inputs");

calculator.setExpression({id: 'graph1', latex: "y=\\sqrt{x}"});
calculator.setExpression({id: 'graph2', latex: "y=x^2"});


// a.observe('numericValue', function() {
//   console.log(a.latex);
// });

function onGraph() {
    if (document.getElementsByClassName("graphic")[0].style.visibility === "visible") {
        document.getElementsByClassName("graphic")[0].style.visibility = "hidden";
        document.getElementById("graphId").innerText = "Show Graphic";
    } else {
        document.getElementsByClassName("graphic")[0].style.visibility = "visible"
        document.getElementById("graphId").innerText = "Hide Graphic";
    }

}


function addInput() {
    var forms = document.querySelector('#id_form-TOTAL_FORMS')
    var newinput = document.querySelector('#id_form-0-equation').cloneNode(true);
    var newlabel = document.createElement("label")

    newlabel.setAttribute("for", 'id_form-' + forms.value + '-equation');
    newlabel.innerText = "Equation: ";


    console.log(forms.value)
    newinput.name = 'form-' + forms.value + '-equation';
    newinput.id = 'id_form-' + forms.value + '-equation';


    var p = document.createElement("p");
    p.appendChild(newlabel);
    p.appendChild(newinput);
    document.querySelector('#formContent').appendChild(p);

    forms.value = parseInt(forms.value) + 1;
}

function deleteInput() {
    var forms = document.querySelector('#id_form-TOTAL_FORMS');
    forms.value = parseInt(forms.value) - 1;
    //
    removeInput = '#id_form-' + forms.value + '-equation';
    document.querySelector(removeInput).remove();
    var labels = document.getElementsByTagName("label");
    for (var i = 0; i < labels.length; i++) {
        if (labels[i].getAttribute("for") === 'id_form-' + forms.value + '-equation') {
            labels[i].parentNode.remove();
        }
    }

}



