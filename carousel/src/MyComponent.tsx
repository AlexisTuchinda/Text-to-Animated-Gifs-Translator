
import "./MyComponent.css";
import {
  StreamlitComponentBase,
  withStreamlitConnection,
} from "streamlit-component-lib"
import React, { ReactNode } from "react";
import Carousel from 'react-bootstrap/Carousel';
interface State {
  isFocused: boolean,
  currentCaption: string,
  index: number
}
class MyComponent extends StreamlitComponentBase<State> {
  public state = { isFocused: false, currentCaption: "", index: 0 };
  public render = (): ReactNode => {
// THE BELOW LINES ARE FROM THE TEMPLATE COMPONENT PROVIDED BY STREAMLIT
    // Streamlit sends us a theme object via props that we can use to ensure
    // that our component has visuals that match the active theme in a
    // streamlit app.
    const { theme } = this.props
    const style: React.CSSProperties = {}
    // Maintain compatibility with older versions of Streamlit that don't send
    // a theme object.
    if (theme) {
      // Use the theme object to style our button border. Alternatively, the
      // theme style is defined in CSS vars.
      const borderStyling = `1px solid ${
        this.state.isFocused ? theme.primaryColor : "gray"
      }`
      style.outline = borderStyling
    }
// END ABOVE STATEMENT

    return (
      <div>
        <Carousel 
          slide={false}
          // variant="dark"
          interval={null}
          style={{width:"auto", height:this.props.args["height"]}}
        >
          {this.props.args["urls"].map((url: string, index: number) => {
            return (
              <Carousel.Item>
                <img
                  className="d-block w-100 h-100"
                  src={url}
                  alt={"carousel element"}
                  style={{width:"auto", height:"auto"}}
                />
                <Carousel.Caption className="caption">
                  <h4>{this.props.args["prompts"][index]}</h4>
                </Carousel.Caption>
              </Carousel.Item>
            )
          })}
        </Carousel>
      </div>
    )
  }
}

export default withStreamlitConnection(MyComponent)
