import React, { Component } from "react";
import { render } from "react-dom";

import { ChakraProvider, Button, List, ListItem, Divider } from '@chakra-ui/react'

class ViewCities extends Component {
  constructor(props) {
    super(props);
    this.state = {
      data: [],
      cityData : [], //Array to hold returned cities
      cityDataLoaded : false,
      loaded: false,
      placeholder: "Loading",
      myNumber: 1
    };

    this.onClickViewAllCities = this.onClickViewAllCities.bind(this);
    this.clearCities = this.clearCities.bind(this);
  }

  handleClick() {
    this.setState(state => ({
        myNumber: state.myNumber + 5
    }));
    }

    clearCities(){
        this.setState(state => (
            { cityData : [] }
        ))
    }
    onClickViewAllCities()
    {
        fetch("http://127.0.0.1:8000/city")
        .then(response => {
          if (response.status > 400) {
            return this.setState(() => {
              return { placeholder: "Something went wrong!" };
            });
          }
          return response.json();
        })
        .then(cityData => {
          this.setState(() => {
            return {
              cityData,
              cityDataLoaded: true
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
            <Button onClick={this.onClickViewAllCities}>
                {"Load Cities"}
            </Button>    
            <Button onClick={this.clearCities}>
                {"Clear Cities"}
            </Button>
            <hr class="dotted" />      
        <ul>
        {
                this.state.cityData.map(cityDatum => {
                    return (   <li key={cityDatum.name}>
                        {cityDatum.name} | latitude:{cityDatum.latitude} | longitude: {cityDatum.longitude}
                    </li>
                    );
                })
        }
      </ul>
      </div>
    );
  }
}


export default ViewCities;

const container = document.getElementById("viewCities");
render(<ViewCities />, container);


