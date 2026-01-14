local leap_year = function(year)
    if year % 4 ~= 0 then
        return false
    elseif year % 100 ~= 0 then
        return true
    elseif year % 400 == 0 then
        return true
    else
        return false
    end
end

return leap_year