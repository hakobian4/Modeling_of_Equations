var elt = document.getElementById('calculator');
var calculator = Desmos.GraphingCalculator(elt);
var a = document.getElementById("inputs");

calculator.setExpression({ id: 'graph1', latex: a });


a.observe('numericValue', function() {
  console.log(a.latex);
});