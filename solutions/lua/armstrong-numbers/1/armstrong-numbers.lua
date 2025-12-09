local ArmstrongNumbers = {}

function ArmstrongNumbers.is_armstrong_number(number)
    local digits = tostring(number)
    local power = #digits

    local sum = 0
    for i = 1, power do
        local digit = tonumber(digits:sub(i, i))
        sum = sum + digit ^ power
    end

    return sum == number
end

return ArmstrongNumbers
