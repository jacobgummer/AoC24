module Utils
export get_lines_from_file

function get_lines_from_file(filename::String)
  lines = open(filename) do file
    readlines(file)
  end
  return lines
end
end
