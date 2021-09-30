import logo from './logo.svg';
import './App.css';
import React, {useState} from "react";

function App() {

	const [state, setstate] = useState("")

	var ws = new WebSocket("ws://127.0.0.1:5678")
	ws.onmessage = function (event) {
		setstate(event.data);
	}

	return (
		<div className="App">
			<p>{state}</p>
		</div>
	);
}

export default App;
