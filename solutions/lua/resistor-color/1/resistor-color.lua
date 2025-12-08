return {
  color_code = function(color)
        local colors = {
      "black",
      "brown",
      "red",
      "orange",
      "yellow",
      "green",
      "blue",
      "violet",
      "grey",
      "white"
    }

    for i, c in ipairs(colors) do
      if c == color then
        return i - 1
      end
    end
  end
}
