module Utils
export get_lines

function get_lines(filename::String)
  lines = open(filename) do file
    readlines(file)
  end
  return lines
end
end
