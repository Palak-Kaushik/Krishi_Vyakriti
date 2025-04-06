import streamlit as st
from components.header import render_header, show_extra_menu
from components.back_button import back_to_dashboard

def opportunities_page():
    render_header()
    show_extra_menu()
    
    st.title("Opportunities for Farmers")
    st.subheader("Support programs and financial assistance available for you")
    
    tab1, tab2, tab3 = st.tabs(["Government Initiatives", "Financial Support", "Insurance Programs"])
    
    with tab1:
        st.markdown("## Government Initiatives and Schemes")
        
        # Display government schemes
        schemes = [
            {
                "name": "PM-KISAN (Pradhan Mantri Kisan Samman Nidhi)",
                "description": "Direct income support of ₹6,000 per year to eligible farmer families in three equal installments.",
                "eligibility": "Small and marginal farmers with cultivable landholding up to 2 hectares.",
                "link": "https://pmkisan.gov.in/"
            },
            {
                "name": "Kisan Credit Card (KCC)",
                "description": "Provides farmers with short-term credit for cultivation and other needs at subsidized interest rates.",
                "eligibility": "All farmers, sharecroppers, and tenant farmers.",
                "link": "https://www.nabard.org/content.aspx?id=593"
            },
            {
                "name": "Soil Health Card Scheme",
                "description": "Soil testing and recommendations for appropriate nutrient usage to improve productivity.",
                "eligibility": "All farmers with land records.",
                "link": "https://soilhealth.dac.gov.in/"
            },
            {
                "name": "National Mission for Sustainable Agriculture (NMSA)",
                "description": "Promotes sustainable farming practices through soil and water conservation methods.",
                "eligibility": "Farmers willing to adopt conservation technologies.",
                "link": "https://nmsa.dac.gov.in/"
            }
        ]
        
        for scheme in schemes:
            with st.expander(scheme["name"]):
                st.markdown(f"**Description:** {scheme['description']}")
                st.markdown(f"**Eligibility:** {scheme['eligibility']}")
                st.markdown(f"**Learn more:** [{scheme['name']}]({scheme['link']})")
                st.markdown("---")
    
    with tab2:
        st.markdown("## Financial Support")
        
        # Display financial institutions and programs
        st.markdown("### Banking Programs for Farmers")
        
        banks = [
            {
                "name": "NABARD (National Bank for Agriculture and Rural Development)",
                "programs": [
                    "Rural Infrastructure Development Fund (RIDF)",
                    "Refinance for farm mechanization",
                    "Long-term agricultural loans at concessional rates"
                ],
                "link": "https://www.nabard.org/farmers-corner"
            },
            {
                "name": "SBI Agricultural Loans",
                "programs": [
                    "Crop loans with interest subvention",
                    "Farm equipment loans",
                    "Land development loans",
                    "Warehouse receipt financing"
                ],
                "link": "https://sbi.co.in/web/agri-rural/agriculture-banking"
            },
            {
                "name": "Microfinance Institutions",
                "programs": [
                    "Group-based lending for small farmers",
                    "Joint liability group loans",
                    "Self-help group financing"
                ],
                "link": "#"
            }
        ]
        
        for bank in banks:
            with st.expander(bank["name"]):
                st.markdown("**Available Programs:**")
                for program in bank["programs"]:
                    st.markdown(f"- {program}")
                st.markdown(f"**Learn more:** [{bank['name']}]({bank['link']})")
                st.markdown("---")
        
        st.markdown("### Interest Subvention Schemes")
        st.info("Agricultural loans up to ₹3 lakhs are available at concessional interest rates of 4% for prompt repayment, with an additional 3% subvention for timely repayment.")
        
    with tab3:
        st.markdown("## Insurance Programs")
        
        # Display insurance schemes
        insurance = [
            {
                "name": "Pradhan Mantri Fasal Bima Yojana (PMFBY)",
                "description": "Comprehensive crop insurance to cover yield losses due to non-preventable risks like natural calamities.",
                "premium": "Farmers pay 1.5% to 2% of sum insured for kharif crops, 1.5% for rabi crops, and 5% for commercial/horticultural crops.",
                "link": "https://pmfby.gov.in/"
            },
            {
                "name": "Weather Based Crop Insurance Scheme (WBCIS)",
                "description": "Insurance against adverse weather conditions that are deemed to impact crop production.",
                "premium": "Similar to PMFBY with government subsidizing the premium balance.",
                "link": "https://agricoop.nic.in/en/divisiontype/agricultural-insurance"
            },
            {
                "name": "Coconut Palm Insurance Scheme",
                "description": "Insurance coverage for coconut palm growers against natural calamities and other perils.",
                "premium": "Premium sharing between farmers, central and state governments.",
                "link": "https://coconutboard.gov.in/presentation/insurance-scheme.aspx"
            }
        ]
        
        for ins in insurance:
            with st.expander(ins["name"]):
                st.markdown(f"**Description:** {ins['description']}")
                st.markdown(f"**Premium:** {ins['premium']}")
                st.markdown(f"**Learn more:** [{ins['name']}]({ins['link']})")
                st.markdown("---")
    
    # Application process section
    st.markdown("## How to Apply")
    st.info("Visit your nearest Krishi Vigyan Kendra, Common Service Center, or District Agriculture Office to get assistance with applications for these schemes.")
    
    # Eligibility checker tool
    st.markdown("## Eligibility Checker")
    st.write("Find out which schemes you might be eligible for by answering a few questions:")
    
    landholding = st.slider("What is your total landholding in acres?", 0.0, 20.0, 2.0, 0.5)
    crop_type = st.selectbox("What is your main crop type?", ["Rice", "Wheat", "Pulses", "Oilseeds", "Vegetables", "Fruits", "Other"])
    
    if st.button("Check Eligibility"):
        st.success(f"Based on your inputs, you may be eligible for:")
        if landholding <= 5:
            st.write("- PM-KISAN")
            st.write("- Pradhan Mantri Fasal Bima Yojana")
            st.write("- Kisan Credit Card with higher subsidies")
        else:
            st.write("- Kisan Credit Card")
            st.write("- Agricultural Infrastructure Fund")
            
        if crop_type in ["Vegetables", "Fruits"]:
            st.write("- National Horticulture Mission subsidies")
            st.write("- Cold storage subsidy schemes")
    
    # Contact information
    st.markdown("## Need Help?")
    st.write("Contact your local Agriculture Department or call our helpline:")
    st.code("Kisan Call Center: 1800-180-1551")
    
    back_to_dashboard()

if __name__ == "__main__":
    opportunities_page()