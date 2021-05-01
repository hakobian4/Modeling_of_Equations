var elt = document.getElementById('calculator');
var calculator = Desmos.GraphingCalculator(elt);
var a = document.getElementById("inputs");
var currentInputId;


calculator.setExpression({id: 'graph1', latex: "y=\\sqrt{x}"});
calculator.setExpression({id: 'graph2', latex: "y=x^2"});

// a.observe('numericValue', function() {
//   console.log(a.latex);
// });

function onGraph() {
    if (document.getElementsByClassName("graphic")[0].style.visibility === "visible") {
        document.getElementsByClassName("graphic")[0].style.visibility = "hidden";
        document.getElementById("graphId").querySelector("span").innerText = "Show Graphic";
    } else {
        document.getElementsByClassName("graphic")[0].style.visibility = "visible"
        document.getElementById("graphId").querySelector("span").innerText = "Hide Graphic";
    }

}


function addInput() {
    var forms = document.querySelector('#id_form-TOTAL_FORMS')
    var newinput = document.querySelector('#id_form-0-equation').cloneNode(true);
    var newlabel = document.createElement("label")

    newlabel.setAttribute("for", 'id_form-' + forms.value + '-equation');
    newlabel.innerText = "Equation: ";

    newinput.name = 'form-' + forms.value + '-equation';
    newinput.id = 'id_form-' + forms.value + '-equation';
    newinput.value = '';


    var p = document.createElement("p");
    p.appendChild(newlabel);
    p.appendChild(newinput);
    document.querySelector('#formContent').appendChild(p);

    forms.value = parseInt(forms.value) + 1;
}

function deleteInput() {
    var forms = document.querySelector('#id_form-TOTAL_FORMS');
    if (forms.value > 1) {
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
}

function clearInput() {
    var forms = document.querySelector('#id_form-TOTAL_FORMS');
    for (var j = 1; j < forms.value; j++) {
        // forms.value = parseInt(forms.value) - 1;
        //
        removeInput = '#id_form-' + j + '-equation';
        document.querySelector(removeInput).remove();
        var labels = document.getElementsByTagName("label");
        for (var i = 0; i < labels.length; i++) {
            if (labels[i].getAttribute("for") === 'id_form-' + j + '-equation') {
                labels[i].parentNode.remove();
            }
        }
    }
    document.getElementById('id_form-0-equation').value = '';
    forms.value = 1;
    console.log(document.getElementsByClassName("answers")[0].innerHTML = '');
}

function checkEmpty() {

}


function math_function(f) {
    let elem = document.getElementById(currentInputId);
    let curPos = elem.selectionStart;
    elem.value = elem.value.slice(0, curPos) + f + elem.value.slice(curPos);
    elem.focus()
    elem.selectionStart = elem.selectionEnd = curPos + f.length;
}


function squarerootInput() {
    math_function("sqrt(x)");
}

function nthsquarerootInput() {
    math_function("x^(1/n)");
}


function degreeInput() {
    math_function("(x)^(n)");
}

function exponentInput() {
    math_function("(n)^(x)");
}

function logInput() {
    math_function("log(b,a)")
}

function piInput() {
    math_function("pi")
}

function eInput() {
    math_function("e")
}


$(document).ready(function () {

    $("p input").on("focus", function (e) {
        currentInputId = e.target.id;
        console.log(currentInputId);
    });
});

// function checkEmptry(){
//     var forms = document.querySelector('#id_form-TOTAL_FORMS');
//     for (let i = 0; i < forms.value; i++) {
//         let removeInput = '#id_form-' + i + '-equation';
//         if (removeInput.value === undefined) {
//             console.log("aasss", typeof removeInput.value);
//
//             this.type = "button";
//         } else {
//             console.log("aasss", typeof removeInput.value);
//
//             this.type = "submit";
//             break;
//         }
//     }
//     console.log("aa", this.type);
// }

