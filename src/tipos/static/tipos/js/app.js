console.log("hello");

// Valores de inicio y globales
var startNode = "A";
var newNodes = ["A", "B", "C", "D"];
var newEdges = [
  ["A", "B"],
  ["A", "C"],
  ["B", "C"],
  ["B", "D"],
  ["C", "D"]
];
// var newWeights = [3, 2, 1, 2, 3];

// Funcion para aumentar una letra: B+1 => C
function nextChar(c) {
  return String.fromCharCode(c.charCodeAt(0) + 1);
}

// Parte principal
document.addEventListener("DOMContentLoaded", function() {
  var cy = (window.cy = cytoscape({
    container: document.getElementById("cy"),

    // Layout para los nodos iniciales
    layout: {
      name: "grid",
      rows: 3,
      cols: 2
    },

    // Tomado los estilos del json
    style: [
      {
        selector: "node",
        style: {
          content: "data(name)"
        }
      },

      {
        selector: "edge",
        style: {}
      },

      {
        selector: ".eh-handle",
        style: {
          "background-color": "red",
          width: 12,
          height: 12,
          shape: "ellipse",
          "overlay-opacity": 0,
          "border-width": 12,
          "border-opacity": 0
        }
      },

      {
        selector: ".eh-hover",
        style: {
          "background-color": "red"
        }
      },

      {
        selector: ".eh-source",
        style: {
          "border-width": 2,
          "border-color": "red"
        }
      },

      {
        selector: ".eh-target",
        style: {
          "border-width": 2,
          "border-color": "red"
        }
      },

      {
        selector: ".eh-preview, .eh-ghost-edge",
        style: {
          "background-color": "red",
          "line-color": "red",
          "target-arrow-color": "red",
          "source-arrow-color": "red"
        }
      },

      {
        selector: ".eh-ghost-edge.eh-preview-active",
        style: {
          opacity: 0
        }
      },
      {
        selector: "edge[label]",
        style: {
          label: "data(label)",
          width: 3
        }
      }
    ],

    // Nodos y aristas iniciales
    elements: {
      nodes: [
        { data: { id: "A", name: "A" } },
        { data: { id: "B", name: "B" } },
        { data: { id: "C", name: "C" } },
        { data: { id: "D", name: "D" } }
      ],
      edges: [
        { data: { source: "A", target: "B"} },
        { data: { source: "A", target: "C" } },
        { data: { source: "B", target: "D" } },
        { data: { source: "B", target: "C" } },
        { data: { source: "C", target: "D" } }
      ]
    }
  }));

  var eh = cy.edgehandles();

  // async function getWeight() {
  //   const { value: peso } = await Swal({
  //     title: "Ingrese el peso",
  //     input: "text",
  //     inputPlaceholder: "peso",
  //     inputValidator: value => {
  //       return isNaN(parseInt(value)) && "El peso debe ser un valor numérico";
  //     }
  //   });

  //   return peso;
  // }

  // agregando peso y aristas a los arrays globales
  cy.on("ehcomplete", (event, sourceNode, targetNode, addedEles) => {
    let sourceNodeId = sourceNode._private.data.id;
    let targetNodeId = targetNode._private.data.id;
    // let weight = prompt("Ingrese el peso");

    // getWeight().then(val => {
    //   let weight = val;
      let newEdge = [sourceNodeId, targetNodeId];
      newEdges.push(newEdge);
      // cy.elements().edges()[
      //   cy.elements().edges().length - 1
      // ]._private.data.label = weight;
      // newWeights.push(weight);
      // document.querySelector(".tip").style.visibility = "visible";
    // });
  });

  // Dibujando nodo y agregando a array global
  cy.on("tap", function(evt) {
    var tgt = evt.target;
    let nextNode = startNode;

    if (newNodes.length > 0) {
      nextNode = nextChar(newNodes[newNodes.length - 1]);
    }
    var id = nextNode;

    if (tgt === cy) {
      cy.add({
        classes: "automove-viewport",
        data: { id: id, name: id },
        position: {
          x: evt.position.x,
          y: evt.position.y
        }
      });
      newNodes.push(id);
    }
  });

  // Eliminando nodo
  cy.on("cxttap", "node", function(evt) {
    var tgt = evt.target;
    const nodeId = tgt._private.data.id;
    const index = newNodes.indexOf(nodeId);
    newNodes.splice(index, 1);

    for (let i = 0; i < newEdges.length; i++) {
      if (newEdges[i].includes(nodeId)) {
        newEdges.splice(i, 1);
        // newWeights.splice(i, 1);
        i--;
      }
    }
    tgt.remove();
  });

  function inNodes(node) {
    for (let i = 0; i < newEdges.length; i++) {
      if (newEdges[i].includes(node)) {
        return true;
      }
    }
  }

  // Boton para reiniciar el canvas
  document.querySelector("#reset").addEventListener("click", function() {
    cy.elements().remove();
    newNodes = [];
    newEdges = [];
    // newWeights = [];
  });

  // calulando dijkstra
  document.querySelector("#calcular").addEventListener("click", function() {
    // let inicio = prompt("ingrese el inicio");
    // let final = prompt("Ingrese el final");
    let nodesDict = {};

    for (let i = 0; i < newNodes.length; i++) {
      nodesDict[newNodes[i]] = newNodes[i];
    }

    (async () => {
      const { value: inicio } = await Swal({
        title: "Ingrese el inicio",
        input: "select",
        inputOptions: nodesDict,
        inputPlaceholder: "Nodo",
        inputValidator: value => {
          return new Promise(resolve => {
            if (value && inNodes(value)) {
              resolve();
            } else {
              resolve("Dege elegir un nodo que tenga arista");
            }
          });
        }
      });

      const { value: final } = await Swal({
        title: "Ingrese el destino",
        input: "select",
        inputOptions: nodesDict,
        inputPlaceholder: "Nodo",
        inputValidator: value => {
          return new Promise(resolve => {
            if (value && inNodes(value)) {
              resolve();
            } else {
              resolve("Dege elegir un nodo que tenga arista");
            }
          });
        }
      });
      console.log(inicio, final);

      const url = "http://localhost:8000/tipos/calcular";
      let data = {
        nodos: newNodes,
        aristas: newEdges,
        // pesos: newWeights,
        inicio: inicio.toUpperCase(),
        destino: final.toLocaleUpperCase()
      };
      fetch(url, {
        method: "POST",
        headers: {
          "Content-Type": "application/json",
          "X-Requested-With": "XMLHttpRequest"
        },
        body: JSON.stringify(data)
      })
        .then(res => res.json())
        .then(data => {
          document.querySelector(".respuesta").textContent = ` ${data.camino}  - Peso: ${data.peso}`;
          return data;
        })
        .then(data => console.log(data))
        .catch(err => console.log(err));
    })();
  });
});
