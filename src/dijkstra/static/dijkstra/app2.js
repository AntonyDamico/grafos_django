console.log("hello");

const data = {
  'nodes': ['A', 'B', 'C'],
  'edges': [['A', 'B'], ['B', 'C']],
  'weigths': [1, 2]
};

data2 = {
  hello: 'bye',
  bye: 'hello'
}

console.log(JSON.stringify(data2));

const url = "http://localhost:8000/dijkstra/calcular";




const post_data = () => {
  fetch(url, {
    method: "POST",
    headers: {
      "Content-Type": "application/json",
      'X-Requested-With': 'XMLHttpRequest'
    },
    body: JSON.stringify(data)
  })
    .then(res => res.json())
    .then(data => console.log(data))
    .catch(err => console.log(err));
};


document.querySelector('button').addEventListener('click', post_data)
