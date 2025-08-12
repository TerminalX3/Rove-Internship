'''
This is a file which includes code for synthetic routing and hiden city ticketing code. 
It is unable to be implemented with the free version of Amadeus, however, after minor 
bug fixes it will work with the full paid version of the API.
'''

'''
below is example code for synthetic routing, 
it doesn't actually work with free version of Amadeus, and only uses BCN as a stop, 
but it can be used for any stop, and would need to pass used as a function in algorithm.py
'''

''' 
flights = []

if use_synthetic: ##just example code using BCN
    stop = "BCN"

    try:
        # Leg 1: origin -> BCN
        response1 = self.amadeus.shopping.flight_offers_search.get(
            originLocationCode=origin,
            destinationLocationCode=stop,
            departureDate=departure_date,
            adults=1,
            max=10
        )

        for offer1 in response1.data:
            try:
                price1 = float(offer1['price']['total'])
                airline1 = offer1['itineraries'][0]['segments'][0]['carrierCode']
                duration1 = offer1['itineraries'][0]['duration']
                leg1_arrival_str = offer1['itineraries'][0]['segments'][-1]['arrival']['at']
                leg1_arrival_dt = datetime.fromisoformat(leg1_arrival_str)

                # Leg 2: BCN -> destination
                response2 = self.amadeus.shopping.flight_offers_search.get(
                    originLocationCode=stop,
                    destinationLocationCode=destination,
                    departureDate=departure_date,
                    adults=1,
                    max=10
                )

                for offer2 in response2.data:
                    try:
                        leg2_departure_str = offer2['itineraries'][0]['segments'][0]['departure']['at']
                        leg2_departure_dt = datetime.fromisoformat(leg2_departure_str)

                        if leg2_departure_dt > leg1_arrival_dt:
                            price2 = float(offer2['price']['total'])
                            total_price = price1 + price2
                            currency = offer2['price']['currency']
                            airline2 = offer2['itineraries'][0]['segments'][0]['carrierCode']
                            duration2 = offer2['itineraries'][0]['duration']
                            cabin = offer2['travelerPricings'][0]['fareDetailsBySegment'][0].get('cabin', 'ECONOMY')

                            flight = {
                                'price': total_price,
                                'currency': currency,
                                'airline': f"{airline1} & {airline2}",
                                'duration': f"{duration1} + {duration2}",  # You can combine ISO durations properly later
                                'cabin': cabin,
                                'stopover': stop
                            }

                            flights.append(flight)

                    except Exception as e:
                        print(f"Error in leg 2 loop: {e}")
                        continue

            except Exception as e:
                print(f"Error in leg 1 loop: {e}")
                continue

    except Exception as e:
        print(f"Error fetching synthetic flights: {e}")

'''


'''
below is example code for hidden city ticketing, 
we cannot make it functional in the program since we need flights with 3+ airports -> also needed to bugtest
'''


''' 
flights = []

if use_hidden: ##just example code using BCN
    airports = [BCN, JFK] ##all airports in the world

    for final_dest in airports:

        try:
        # fetching flights
        response = self.amadeus.shopping.flight_offers_search.get(
            originLocationCode=origin,
            destinationLocationCode=stop,
            departureDate=departure_date,
            adults=1,
            max=10
        )

        for offer in response.data{
            for itinerary in offer.get('itineraries', []):
                    segments = itinerary.get('segments', [])

            for segment in segments{
                if segment['arrival']['iataCode'] == destination:
                    flight = {
                                'price': float(offer['price']),
                                'currency': offer['currency'],
                                'airline': offer['airline'],
                                'duration': offer['duration'],
                                'cabin': offer['cabin']
                            }
                    flights.append(flight)
            }

        
        }

    except Exception as e:
        print(f"Error fetching hidden city ticketing flights: {e}")

'''



