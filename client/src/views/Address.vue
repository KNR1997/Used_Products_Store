<script>
import { reactive } from "vue";
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
})

// Api call-> get user address details if present

</script>

<template>
    <div>
        <div 
            id="AddressPage" 
            class="mt-4 max-w-[500px] mx-auto px-2"
        >
            <div class="mx-auto bg-white rounded-lg p-3">
                <div class="text-xl text-bold mb-2">Address Details</div>
                <form @submit.prevent="submit()">
                    <input 
                        class="w-full"
                        placeholder="Contact Name"
                        v-model="contactName"
                        inputType="text"
                        :error="error && error.type == 'contactName' ? error.message : ''"
                    />

                    <input 
                        class="w-full mt-2"
                        placeholder="Address"
                        v-model="address"
                        inputType="text"
                        :error="error && error.type == 'address' ? error.message : ''"
                    />

                    <input 
                        class="w-full mt-2"
                        placeholder="Zip Code"
                        v-model="zipCode"
                        inputType="text"
                        :error="error && error.type == 'zipCode' ? error.message : ''"
                    />

                    <input 
                        class="w-full mt-2"
                        placeholder="City"
                        v-model="city"
                        inputType="text"
                        :error="error && error.type == 'city' ? error.message : ''"
                    />

                    <input 
                        class="w-full mt-2"
                        placeholder="Country"
                        v-model="country"
                        inputType="text"
                        :error="error && error.type == 'country' ? error.message : ''"
                    />

                    <button 
                        :disabled="isWorking"
                        type="submit"
                        class="
                            mt-6
                            bg-gradient-to-r 
                            from-[#FE630C] 
                            to-[#FF3200]
                            w-full 
                            text-white 
                            text-[21px] 
                            font-semibold 
                            p-1.5 
                            rounded-full
                        "
                    >
                        <div v-if="!isWorking">Update Address</div>
                        <Icon 
                            v-else
                            name="eos-icons:loading" 
                            size="25" 
                            class="mr-2"
                        />
                    </button>
                </form>
            </div>
        </div>
    </div>
</template>