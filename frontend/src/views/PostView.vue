<!-- <script setup>
import { reactive } from "vue";
import { useRouter } from 'vue-router';
import axios from "axios";
import { Form, Field, ErrorMessage, useForm } from "vee-validate";
import * as Yup from "yup";
const router=useRouter()
const validationSchema = Yup.object({
  description: Yup.string().required("Description is required!"),
  tag: Yup.string().required("Tag is required!"),
  media: Yup.string().required("Media is required!"),
  location: Yup.string().required("Location is required!"),
  audience: Yup.string().required("Audience is required!"),
});
const formInput = reactive({
  description: "",
  tag: "",
  location: "",
  media: "",
  audience: "",
});

const { handleSubmit } = useForm({
  validationSchema,
});
const onSubmit = async () => {
  try {
    const response = await axios.post("http://localhost:8000/api/posts", {
      description: formInput.description,
      tag: formInput.tag,
      media: formInput.media,
      location: formInput.location,
      audience: formInput.audience,
    });
    if (response.status === 200 || response.status === 201) {
      console.log("Form submitted successfully:", response.data);
      formInput.description = "";
      formInput.tag = "";
      formInput.media = "";
      formInput.location = "";
      formInput.audience = "";
      await router.push('/');
    } else {
      console.error("Error submitting form:", response.data);
      alert("Failed to submit the form. Please try again later.");
    }
  } catch (error) {
    console.error("Error submitting form:", error);
    alert("An error occurred. Please try again later.");
  }
};


</script> -->
<script setup>
import { reactive } from "vue";
import { useRouter } from 'vue-router';
import axios from "axios";
import { Form, Field, ErrorMessage, useForm } from "vee-validate";
import * as Yup from "yup";

const router = useRouter();

const validationSchema = Yup.object().shape({
  description: Yup.string().required("Description is required!"),
  tag: Yup.string().required("Tag is required!"),
  media: Yup.string().required("Media is required!"),
  location: Yup.string().required("Location is required!"),
  audience: Yup.string().required("Audience is required!"),
});

const formInput = reactive({
  description: "",
  tag: "",
  location: "",
  media: "",
  audience: "",
});

const { handleSubmit } = useForm({
  validationSchema,
});

const onSubmit = async () => {
  try {
    const response = await axios.post("http://localhost:8000/api/posts", {
      description: formInput.description,
      tag: formInput.tag,
      media: formInput.media,
      location: formInput.location,
      audience: formInput.audience,
    });
    if (response.status === 200 || response.status === 201) {
      console.log("Form submitted successfully:", response.data);
      formInput.description = "";
      formInput.tag = "";
      formInput.media = "";
      formInput.location = "";
      formInput.audience = "";
      await router.push('/');
      return response;
    } else {
      console.error("Error submitting form:", response.data);
      alert("Failed to submit the form. Please try again later.");
      throw new Error("Failed to submit the form.");
    }
  } catch (error) {
    console.error("Error submitting form:", error);
    alert("An error occurred. Please try again later.");
    throw error;
  }
};
</script>

<template>
  <main
    class="flex flex-col gap-10 mx-10 md:mx-0 px-4 sm:px-8 md:px-12 lg:px-16 xl:px-20 mt-8 sm:mt-12 md:mt-16 lg:mt-20 xl:mt-24"
  >
    <h1 class="text-xl font-semibold">New post</h1>
    <div>
      <h2 class="text-[#C59728] text-lg">Author Name | Published Date</h2>
      <p>
        Please fill content of the new post. It can include text, images, and
        other media. The post should provide valuable information or insights to
        the reader. Additionally, you can select the target audience.
      </p>
    </div>
    <Form :validation-schema="validationSchema"  >
      <div class="flex flex-col gap-5">
        <div class="flex flex-col sm:flex-row gap-5">
          <div class="flex flex-col gap-2 flex-1">
            <Field
              type="text"
              class="px-4 py-3 border-2 rounded-lg outline-none w-full"
              placeholder="What's happening?"
              id="description"
              name="description"
             
              v-model="formInput.description"
            />
            <ErrorMessage name="description" class="text-red-500" />
          </div>
          <div class="flex flex-col gap-2 w-full sm:w-[10rem]">
            <Field
              type="text"
              class="px-4 py-3 border-2 rounded-lg outline-none w-full"
              placeholder="Tag"
              id="tag"
              name="tag"
              v-model="formInput.tag"
            />
            <ErrorMessage name="tag" class="text-red-500" />
          </div>
        </div>
        <div class="flex flex-col sm:flex-row gap-5">
          <div class="flex flex-col gap-2 flex-1">
            <Field
              type="text"
              class="px-4 py-3 border-2 rounded-lg outline-none w-full"
              placeholder="Media"
              id="media"
              name="media"
              v-model="formInput.media"
            />
            <!-- <ErrorMessage name="media" class="text-red-500" /> -->
          </div>
          <div class="flex flex-col gap-2 flex-1">
            <Field
              type="text"
              class="px-4 py-3 border-2 rounded-lg outline-none w-full"
              placeholder="Location"
              id="location"
              name="location"
              v-model="formInput.location"
            />
            <ErrorMessage name="location" class="text-red-500" />
          </div>
          <div class="flex flex-col gap-2 w-full sm:w-[10rem]">
            <select
            
              class="px-4 py-3 border-2 rounded-lg outline-none w-full"
              v-model="formInput.audience"
            >
              <option value="">Public</option>
              <option value="friend">Friend</option>
              <option value="group">Group</option>
            </select>
          </div>
        </div>
      </div>
      <div class="flex justify-end mt-6">
        <button
          type="submit"
          @submit.prevent="onSubmit"
          class="px-8 py-2 rounded-xl border-gray-300 bg-[#008A8A] text-white w-fit"
          
        >
          Post
        </button>
      </div>
    </Form>
  </main>
</template>
<!-- <script setup>
import { reactive } from "vue";
import { useRouter } from 'vue-router';
import axios from "axios";
import { Form, Field, ErrorMessage, useForm } from "vee-validate";
import * as Yup from "yup";

const router=useRouter()

const validationSchema = Yup.object({
  description: Yup.string().required("Description is required!"),
  tag: Yup.string().required("Tag is required!"),
  media: Yup.string().required("Media is required!"),
  location: Yup.string().required("Location is required!"),
  audience: Yup.string().required("Audience is required!"),
});

const formInput = reactive({
  description: "",
  tag: "",
  location: "",
  media: "",
  audience: "",
});

const { handleSubmit } = useForm({
  validationSchema,
});

const onSubmit = async () => {
  try {
    const response = await axios.post("http://localhost:8000/api/posts/", {
      description: formInput.description,
      tag: formInput.tag,
      media: formInput.media,
      location: formInput.location,
      audience: formInput.audience,
    });
    if (response.status === 200 || response.status === 201) {
      console.log("Form submitted successfully:", response.data);
      formInput.description = "";
      formInput.tag = "";
      formInput.media = "";
      formInput.location = "";
      formInput.audience = "";
      await router.push('/');
    } else {
      console.error("Error submitting form:", response.data);
      alert("Failed to submit the form. Please try again later.");
    }
  } catch (error) {
    console.error("Error submitting form:", error);
    alert("An error occurred. Please try again later.");
  }
};
</script>

<template>
  <main class="flex flex-col gap-10 mx-10 md:mx-0 px-4 sm:px-8 md:px-12 lg:px-16 xl:px-20 mt-8 sm:mt-12 md:mt-16 lg:mt-20 xl:mt-24">
    <h1 class="text-xl font-semibold">New post</h1>
    <div>
      <h2 class="text-[#C59728] text-lg">Author Name | Published Date</h2>
      <p>
        Please fill content of the new post. It can include text, images, and
        other media. The post should provide valuable information or insights to
        the reader. Additionally, you can select the target audience.
      </p>
    </div>
    <Form :validation-schema="validationSchema" @submit="onSubmit">
      <div class="flex flex-col gap-5">
        <div class="flex flex-col sm:flex-row gap-5">
          <div class="flex flex-col gap-2 flex-1">
            <Field
              type="text"
              class="px-4 py-3 border-2 rounded-lg outline-none w-full"
              placeholder="What's happening?"
              id="description"
              name="description"
              :value="formInput.description"
              @input="formInput.description = $event.target.value"
            />
            <ErrorMessage name="description" class="text-red-500" />
          </div>
          <div class="flex flex-col gap-2 w-full sm:w-[10rem]">
            <Field
              type="text"
              class="px-4 py-3 border-2 rounded-lg outline-none w-full"
              placeholder="Tag"
              id="tag"
              name="tag"
              :value="formInput.tag"
              @input="formInput.tag = $event.target.value"
            />
            <ErrorMessage name="tag" class="text-red-500" />
          </div>
        </div>
        <div class="flex flex-col sm:flex-row gap-5">
          <div class="flex flex-col gap-2 flex-1">
            <Field
              type="file"
              class="px-4 py-3 border-2 rounded-lg outline-none w-full"
              placeholder="Media"
              id="media"
              name="media"
              :value="formInput.media"
              @input="formInput.media = $event.target.value"
            />
            <ErrorMessage name="media" class="text-red-500" />
          </div>
          <div class="flex flex-col gap-2 flex-1">
            <Field
              type="text"
              class="px-4 py-3 border-2 rounded-lg outline-none w-full"
              placeholder="Location"
              id="location"
              name="location"
              :value="formInput.location"
              @input="formInput.location = $event.target.value"
            />
            <ErrorMessage name="location" class="text-red-500" />
          </div>
          <div class="flex flex-col gap-2 w-full sm:w-[10rem]">
            <select
              class="px-4 py-3 border-2 rounded-lg outline-none w-full"
              :value="formInput.audience"
              @input="formInput.audience = $event.target.value"
            >
              <option value="">Public</option>
              <option value="friend">Friend</option>
              <option value="group">Group</option>
            </select>
          </div>
        </div>
      </div>
      <div class="flex justify-end mt-6">
        <button
          type="submit"
          class="px-8 py-2 rounded-xl border-gray-300 bg-[#008A8A] text-white w-fit"
        >
          Post
        </button>
      </div>
    </Form>
  </main>
</template> -->
