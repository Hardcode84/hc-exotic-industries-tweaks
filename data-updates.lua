
-- Make hydrogen and isotopes burnable
data.raw.fluid["ei_hydrogen-gas"].fuel_value = "20KJ"
data.raw.fluid["ei_protium"].fuel_value = "10KJ"
data.raw.fluid["ei_deuterium"].fuel_value = "10KJ"
data.raw.fluid["ei_tritium"].fuel_value = "10KJ"


-- Loose some lead coolant on each cycle
data.raw.recipe["ei_coolant-exchange"].results =
    {
        {type = "fluid", name = "ei_cold-coolant", amount = 24},
        {type = "fluid", name = "ei_critical-steam", amount = 25},
    }
