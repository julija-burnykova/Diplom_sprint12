-- Задание №1

select c."login", count(o."inDelivery") FROM "Couriers" as c INNER JOIN "Orders" AS o ON c.id = o."courierId" WHERE o."inDelivery" = TRUE GROUP BY o."inDelivery", c."login";

-- Задание №2

select "Orders".track,  CASE WHEN "Orders".finished = TRUE THEN 2 WHEN "Orders".cancelled = TRUE THEN -1 WHEN "Orders"."inDelivery" = True THEN 1 ELSE 0 END FROM "Orders";