import streamlit as st

chosen_tpm = st.selectbox(
    label='Choose TPM',
    help='Bla bla',
    options=('TPM 1', 'TPM 2', 'TPM 3', 'TPM 4', 'TPM 5'),
)

def make_wp_options():
    if chosen_tpm == 'TPM 1':
        return ('WP 1', 'WP 2')
    if chosen_tpm == 'TPM 2':
        return ('EMOTIONS', 'GLOBALIZATION', 'CLIMATE THREATS', 'RESOURCE EXPLOITATION')
    if chosen_tpm == 'TPM 3':
        return ('WP 3', 'WP 4', 'WP 5')
    if chosen_tpm == 'TPM 4':
        return ('WP 6', 'WP 7', 'WP 8')
    if chosen_tpm == 'TPM 5':
        return ('WP 9', 'WP 10',)
    return None

chosen_wp = st.selectbox(
    label='Choose Workpackage',
    help='Bla bla',
    placeholder='Choose TPM first',
    index=None,
    # options=('Emotions', 'WP 2', 'WP 3', 'WP 4', 'WP 5'),
    options=make_wp_options(),
)

# st.info('EMOTIONS')
# st.info('GLOBALIZATION')
# st.info('CLIMATE THREATS')
# st.info('RESOURCE EXPLOITATION')

uploaded_file = st.file_uploader(
    label='Upload PDF',
    accept_multiple_files=False,
    type='pdf',
)

