<script setup>
import { onMounted, reactive } from "vue";
import { authStore } from "../store/store";

const state = reactive({
  contactName: null,
  address: null,
  zipCode: null,
  city: null,
  country: null,

  currentAddress: null,
  isUpdate: null,
  isWorking: null,
  error: null,
});

// Api call-> get user address details if present
onMounted(async () => {
  const user = authStore().getUser();

  try {
    const response = await fetch(
      `http://127.0.0.1:8000/api/get-address/${user.user_id}`
    );
    const result = await response.json();
    if (result) {
      state.contactName = result.contact_name;
      state.address = result.address;
      state.zipCode = result.zip_code;
      state.city = result.city;
      state.country = result.country;

      state.isUpdate = true;
    }
    console.log(result);
  } catch (error) {
    console.error(error);
  }
});

const submit = async () => {
    state.isWorking = true
    state.error = null

  // Validate if all required fields are filled
  if (!state.contactName || !state.address || !state.zipCode || !state.city || !state.country) {
    state.error = {
      type: 'general',
      message: 'All fields are required'
    };
    state.isWorking = false;
    return;
  }

  try {
    const user = authStore().getUser();

    // Construct the request payload
    const payload = {
      user_id: user.user_id,
      contact_name: state.contactName,
      address: state.address,
      zip_code: state.zipCode,
      city: state.city,
      country: state.country,
    };

    // Determine the API endpoint based on whether it's an update or create
    const endpoint = `http://127.0.0.1:8000/api/save-user-address/${user.user_id}`;

    // Make the API call
    const response = await fetch(endpoint, {
      method: state.isUpdate ? 'PUT' : 'POST',
      headers: {
        'Content-Type': 'application/json',
      },
      body: JSON.stringify(payload),
    });

    // Check if the request was successful
    if (response.ok) {
      console.log('Address submitted successfully');
      // Optionally, update the state or perform other actions upon successful submission
    } else {
      console.error('Failed to submit address');
      state.error = {
        type: 'api',
        message: 'Failed to submit address. Please try again later.',
      };
    }
  } catch (error) {
    console.error('Error during address submission', error);
    state.error = {
      type: 'api',
      message: 'An error occurred. Please try again later.',
    };
  } finally {
    state.isWorking = false;
  }
}
</script>

<template>
  <div>
    <div id="AddressPage" class="mt-4 max-w-[500px] mx-auto px-2">
      <div class="mx-auto bg-white rounded-lg p-3">
        <div class="text-xl text-bold mb-2">Address Details</div>
        <form @submit.prevent="submit()">
          <input
            class="w-full"
            placeholder="Contact Name"
            v-model="state.contactName"
            inputType="text"
            :error="error && error.type == 'contactName' ? error.message : ''"
          />

          <input
            class="w-full mt-2"
            placeholder="Address"
            v-model="state.address"
            inputType="text"
            :error="error && error.type == 'address' ? error.message : ''"
          />

          <input
            class="w-full mt-2"
            placeholder="Zip Code"
            v-model="state.zipCode"
            inputType="text"
            :error="error && error.type == 'zipCode' ? error.message : ''"
          />

          <input
            class="w-full mt-2"
            placeholder="City"
            v-model="state.city"
            inputType="text"
            :error="error && error.type == 'city' ? error.message : ''"
          />

          <input
            class="w-full mt-2"
            placeholder="Country"
            v-model="state.country"
            inputType="text"
            :error="error && error.type == 'country' ? error.message : ''"
          />

          <button
            :disabled="isWorking"
            type="submit"
            class="mt-6 bg-gradient-to-r from-[#FE630C] to-[#FF3200] w-full text-white text-[21px] font-semibold p-1.5 rounded-full"
          >
            <div v-if="!isWorking">Update Address</div>
            <Icon v-else name="eos-icons:loading" size="25" class="mr-2" />
          </button>
        </form>
      </div>
    </div>
  </div>
</template>
