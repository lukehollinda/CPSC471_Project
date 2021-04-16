import React, { Component } from "react";
import { render } from "react-dom";

import { ChakraProvider, Button, List, ListItem, Divider } from '@chakra-ui/react'

class ViewNeighborhoods extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
      neighborData : [], //Array to hold returned cities
      neighborDataDataLoaded : false,
      loaded: false,
      placeholder: "Loading",
      myNumber: 1
    };

    this.onClickViewAllNeighborData = this.onClickViewAllNeighborData.bind(this);
    this.clearNeighborData = this.clearNeighborData.bind(this);
  }



    clearNeighborData(){
        this.setState(state => (
            { neighborData : [] }
        ))
    }
    onClickViewAllNeighborData()
    {
        fetch("http://127.0.0.1:8000/neighborhood/")
        .then(response => {
          if (response.status > 400) {
            return this.setState(() => {
              return { placeholder: "Something went wrong!" };
            });
          }
          return response.json();
        })
        .then(neighborData => {
          this.setState(() => {
            return {
              neighborData,
              neighborDataLoaded: true
            };
          });
        });    
    }

    

  componentDidMount() {
    // fetch("http://127.0.0.1:8000/city")
    //   .then(response => {
    //     if (response.status > 400) {
    //       return this.setState(() => {
    //         return { placeholder: "Something went wrong!" };
    //       });
    //     }
    //     return response.json();
    //   })
    //   .then(data => {
    //     this.setState(() => {
    //       return {
    //         data,
    //         loaded: true
    //       };
    //     });
    //   });
  }

  render() {
    return (
        <div>
            <Button onClick={this.onClickViewAllNeighborData}>
                {"Load Neighborhoods"}
            </Button>    
            <Button onClick={this.clearNeighborData}>
                {"Clear Neighborhoods"}
            </Button>
            <hr class="dotted" />      
        <ul>
        {
                this.state.neighborData.map(neighborDatum => {
                    return (   <li key={neighborDatum.name}>
                        {neighborDatum.name} | City: {neighborDatum.cityName}
                    </li>
                    );
                })
        }
      </ul>
      </div>
    );
  }
}


export default ViewNeighborhoods;

const container = document.getElementById("viewNeighborhoods");
render(<ViewNeighborhoods />, container);


