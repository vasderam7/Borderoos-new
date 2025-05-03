
import streamlit as st
import json

# Load itinerary data
with open("borderoos_airasia_demo.json") as f:
    itinerary = json.load(f)

# App branding
st.set_page_config(page_title="Borderoos MVP", layout="centered")
st.title("🦘 Borderoos Travel Concierge")
st.subheader("Your Trip, Beautifully Organised")

# Sidebar Navigation
st.sidebar.title("Navigation")
page = st.sidebar.radio("Go to", ["Itinerary", "Add Protection Confirmation"])

# Show Itinerary Page
if page == "Itinerary":
    st.markdown(f"**Traveller:** {itinerary['traveller_name']}  
**Booking Ref:** `{itinerary['booking_reference']}`")
    st.markdown("---")

    # Display Flights
    for idx, flight in enumerate(itinerary["flights"]):
        with st.expander(f"✈️ Flight {idx+1}: {flight['flight_number']}"):
            st.markdown(f"**Airline:** {flight['airline']}")
            st.markdown(f"**From:** {flight['departure_airport']}")
            st.markdown(f"**To:** {flight['arrival_airport']}")
            st.markdown(f"🕒 **Departs:** {flight['departure_time']}")
            st.markdown(f"🕓 **Arrives:** {flight['arrival_time']}")
            st.markdown(f"💺 **Seat:** {flight['seat']}")
            st.markdown(f"🧳 **Baggage:** {flight['baggage']}")
            st.markdown(f"🍱 **Meal:** {flight['meal']}")
            st.markdown("🔒 **Add-ons:**")
            for addon in flight["addons"]:
                st.markdown(f"- {addon}")

    # Display Layover
    layover = itinerary["layover"]
    st.markdown("---")
    st.markdown(f"🛑 **Layover in {layover['location']}** — Duration: {layover['duration']}")

    # Embedded Protection Prompt
    st.markdown("---")
    st.markdown("## 🛡️ Embedded Protection Options")
    st.info("You're travelling internationally with a long overnight layover. We recommend the following add-ons:")

    col1, col2, col3 = st.columns(3)
    with col1:
        if st.button("Add Travel Delay Cover ($12)"):
            st.session_state.protection = "Travel Delay"
            st.session_state.confirmation = "Travel Delay Cover added for $12."
            st.experimental_set_query_params(page="confirm")

    with col2:
        if st.button("Add Medical Cover ($29)"):
            st.session_state.protection = "Medical"
            st.session_state.confirmation = "International Medical Cover added for $29."
            st.experimental_set_query_params(page="confirm")

    with col3:
        if st.button("Add Baggage Cover ($9)"):
            st.session_state.protection = "Baggage"
            st.session_state.confirmation = "Baggage Protection added for $9."
            st.experimental_set_query_params(page="confirm")

# Confirmation Page
elif page == "Add Protection Confirmation":
    st.success("✅ Protection Added Successfully!")
    confirmation = st.session_state.get("confirmation", "No protection was selected.")
    st.markdown(f"**{confirmation}**")
    st.markdown("You can now travel with peace of mind knowing Roos has your back.")
    if st.button("← Back to Itinerary"):
        st.experimental_set_query_params(page="Itinerary")
