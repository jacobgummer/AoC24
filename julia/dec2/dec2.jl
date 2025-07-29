include("../utils.jl")
using .Utils: get_lines

which_task = length(ARGS) >= 1 ? strip(ARGS[1]) : error("specify which task to do (t1 or t2)")
is_test = false
if length(ARGS) == 2
  is_test = ARGS[2] == "test" ? true : error("snd argument must be \"test\" to do test")
end

lines = is_test ? get_lines("test.txt") : get_lines("input.txt")

function task1()
  processed = [split(l) for l in lines]
  reports = [map(lvl -> parse(Int64, lvl), line) for line in processed]
  count = 0
  for r ∈ reports
    n = length(r)
    diffs = [r[i+1] - r[i] for i in 1:n-1]
    increasing = map(d -> 1 <= d <= 3, diffs)
    if all(increasing) || all(map(d -> -3 <= d <= -1, diffs))
      count += 1
    end
  end
  return count
end

function task2()
  function analyze_report(r)
    n = length(r)
    diffs = [r[i+1] - r[i] for i in 1:n-1]
    increasing = map(d -> 1 <= d <= 3, diffs)
    decreasing = map(d -> -3 <= d <= -1, diffs)
    return all(increasing) || all(decreasing)
  end
  processed = [split(l) for l in lines]
  reports = [map(lvl -> parse(Int64, lvl), line) for line in processed]
  count = 0
  for r ∈ reports
    tolerated = false
    for i ∈ eachindex(r)
      mended = [r[1:i-1]; r[i+1:end]]
      if analyze_report(mended)
        tolerated = true
        break
      end
    end
    count = tolerated ? count + 1 : count
  end
  return count
end

if which_task == "t1"
  println("$(task1())")
elseif which_task == "t2"
  println("$(task2())")
else
  error("must be t1 or t2")
end

