return {
  value = function(colors)
    local map = {
      black = 0,
      brown = 1,
      red = 2,
      orange = 3,
      yellow = 4,
      green = 5,
      blue = 6,
      violet = 7,
      grey = 8,
      white = 9
    }

    local first = map[colors[1]]
    local second = map[colors[2]]

    return first * 10 + second
    
  end
}
