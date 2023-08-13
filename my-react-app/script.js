// ... (existing script content) ...

// Show modal when verify button is clicked
const verifyButtons = document.querySelectorAll('.verify-button');
const modal = document.getElementById('verify-modal');
const closeModal = document.getElementById('close-modal');

verifyButtons.forEach(button => {
  button.addEventListener('click', () => {
    modal.style.display = 'block';
  });
});

closeModal.addEventListener('click', () => {
  modal.style.display = 'none';
});

// Handle form submission
const verifyForm = document.querySelector('.verify-form');

verifyForm.addEventListener('submit', (e) => {
  e.preventDefault();

  const verificationStatus = document.getElementById('verification-status').value;
  const verificationComments = document.getElementById('verification-comments').value;

  // Perform actions based on verification status and comments
  if (verificationStatus === 'accurate') {
    alert('Data verified as accurate.');
  } else if (verificationStatus === 'changes') {
    alert('Changes proposed: ' + verificationComments);
  }

  // Close the modal
  modal.style.display = 'none';
});
