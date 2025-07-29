include("../utils.jl")
using .Utils: get_lines_from_file

which_task = length(ARGS) >= 1 ? strip(ARGS[1]) : error("specify which task to do (t1 or t2)")
is_test = false
if length(ARGS) == 2
  is_test = ARGS[2] == "test" ? true : error("snd argument must be \"test\" to do test")
end

lines = is_test ? get_lines_from_file("test.txt") : get_lines_from_file("input.txt")

function task1()

end

function task2()

end

if which_task == "t1"
  println("$(task1())")
elseif which_task == "t2"
  println("$(task2())")
else
  error("must be t1 or t2")
end
