import React from "react";
import { shallow } from "enzyme";
import Movie from "./Movie";

describe("Movie", () => {
  test("matches snapshot", () => {
    const wrapper = shallow(<Movie />);
    expect(wrapper).toMatchSnapshot();
  });
});
