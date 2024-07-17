<!-- <script setup>
import { reactive, toRefs } from "vue";
import { useRouter } from "vue-router";
import axios from "axios";
import { Form, Field, ErrorMessage, useForm } from "vee-validate";
import * as Yup from "yup";

const router = useRouter();

const validationSchema = Yup.object({
  title: Yup.string().nullable(),
  description: Yup.string().required("Description is required!"),
  tags: Yup.string().required("Tags are required!"),
  media: Yup.string().nullable(),
  location: Yup.string().nullable(),
  audience: Yup.string().required("Audience is required!"),
});

const formInput = reactive({
  title: "",
  description: "",
  tags: "",
  media: "",
  location: "",
  audience: "",
});

const { handleSubmit } = useForm({
  validationSchema,
});

const onSubmit = handleSubmit(async () => {
  const formData = new FormData();
  formData.append("title", formInput.title);
  formData.append("description", formInput.description);
  formData.append("tags", formInput.tags);
  formData.append("media", formInput.media);
  formData.append("location", formInput.location);
  formData.append("audience", formInput.audience);
  try {
    console.log("Submitting form with data:", formInput);

    const response = await axios.post('api/posts/', formData);
    console.log("Response received:", response);

    if (response.status === 200 || response.status === 201) {
      console.log("Form submitted successfully:", response.data);
      formInput.title = "";
      formInput.description = "";
      formInput.tags = "";
      formInput.media = "";
      formInput.location = "";
      formInput.audience = "";
      await router.push("/");
    } else {
      console.error("Error submitting form:", response.data);
      alert("Failed to submit the form. Please try again later.");
    }
  } catch (error) {
    console.error("Error submitting form:", error);
    alert("An error occurred. Please try again later.");
  }
});
const handleMediaUpload = (event) => {
  formInput.media = event.target.files[0];
};
</script>

<template>
  <main
    class="flex flex-col gap-10 mx-10 md:mx-0 px-4 sm:px-8 md:px-12 lg:px-16 xl:px-20 mt-8 sm:mt-12 md:mt-16 lg:mt-20 xl:mt-24"
  >
    <h1 class="text-xl font-semibold">New Post</h1>
    <div>
      <h2 class="text-[#C59728] text-lg">Author Name | Published Date</h2>
      <p>
        Please fill the content of the new post. It can include text, images,
        and other media. The post should provide valuable information or
        insights to the reader. Additionally, you can select the target
        audience.
      </p>
    </div>
    <Form :validation-schema="validationSchema" @submit="onSubmit">
      <div class="flex flex-col gap-5">
        <div class="flex flex-col sm:flex-row gap-5">
          <div class="flex flex-col gap-2 flex-1">
            <Field
              type="text"
              class="px-4 py-3 border-2 rounded-lg outline-none w-full"
              placeholder="Title (Optional)"
              id="title"
              name="title"
              v-model="formInput.title"
            />
            <ErrorMessage name="title" class="text-red-500" />
          </div>
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
        </div>
        <div class="flex flex-col sm:flex-row gap-5">
          <div class="flex flex-col gap-2 flex-1">
            <Field
              type="text"
              class="px-4 py-3 border-2 rounded-lg outline-none w-full"
              placeholder="Tags (comma separated)"
              id="tags"
              name="tags"
              v-model="formInput.tags"
            />
            <ErrorMessage name="tags" class="text-red-500" />
          </div>
          <div class="flex flex-col gap-2 flex-1">
            <Field
              type="file"
              class="px-4 py-3 border-2 rounded-lg outline-none w-full"
              placeholder="Media (Optional)"
              id="media"
              name="media"
              @change="handleMediaUpload"
            />
            <ErrorMessage name="media" class="text-red-500" />
          </div>
        </div>
        <div class="flex flex-col sm:flex-row gap-5">
          <div class="flex flex-col gap-2 flex-1">
            <Field
              type="text"
              class="px-4 py-3 border-2 rounded-lg outline-none w-full"
              placeholder="Location (Optional)"
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
              <option value="public">Public</option>
              <option value="friends">Friends</option>
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


<script setup>
import { reactive, onMounted, onBeforeUnmount } from "vue";
import { useRouter } from "vue-router";
import { Form, Field, ErrorMessage, useForm } from "vee-validate";
import * as Yup from "yup";

const router = useRouter();
const validationSchema = Yup.object({
  title: Yup.string().nullable(),
  description: Yup.string().required("Description is required!"),
  tags: Yup.string().required("Tags are required!"),
  media: Yup.string().nullable(),
  location: Yup.string().nullable(),
  audience: Yup.string().required("Audience is required!"),
});

const formInput = reactive({
  title: "",
  description: "",
  tags: "",
  media: "",
  location: "",
  audience: "",
});

const { handleSubmit } = useForm({ validationSchema });
let websocket;

const connectWebSocket = () => {
  websocket = new WebSocket("ws://localhost:8000/ws/posts/");

  websocket.onopen = () => {
    console.log("WebSocket connection established");
  };

  websocket.onmessage = (message) => {
    console.log("Message from server:", message.data);
  };

  websocket.onerror = (error) => {
    console.error("WebSocket error:", error);
  };

  websocket.onclose = () => {
    console.log("WebSocket connection closed");
  };
};

const onSubmit = handleSubmit(async () => {
  const data = {
    action: 'create',
    post: {
      title: formInput.title,
      description: formInput.description,
      tags: formInput.tags,
      media: formInput.media,
      location: formInput.location,
      audience: formInput.audience,
    },
  };

  try {
    console.log("Submitting form with data:", data);
    websocket.send(JSON.stringify(data));
    console.log("Data sent to WebSocket");

    // Reset form input after sending data
    Object.keys(formInput).forEach(key => {
      formInput[key] = "";
    });

    // Optionally, navigate after submission
    await router.push("/");
  } catch (error) {
    console.error("Error sending data:", error);
    alert("An error occurred. Please try again later.");
  }
});

const handleMediaUpload = (event) => {
  formInput.media = event.target.files[0];
};

// Set up and clean up WebSocket connection
onMounted(connectWebSocket);
onBeforeUnmount(() => {
  if (websocket) {
    websocket.close();
  }
});
</script>

<template>
  <main class="flex flex-col gap-10 mx-10 md:mx-0 px-4 sm:px-8 md:px-12 lg:px-16 xl:px-20 mt-8 sm:mt-12 md:mt-16 lg:mt-20 xl:mt-24">
    <h1 class="text-xl font-semibold">New Post</h1>
    <div>
      <h2 class="text-[#C59728] text-lg">Author Name | Published Date</h2>
      <p>Please fill the content of the new post...</p>
    </div>
    <Form :validation-schema="validationSchema" @submit.prevent="onSubmit">
      <div class="flex flex-col gap-5">
        <div class="flex flex-col sm:flex-row gap-5">
          <div class="flex flex-col gap-2 flex-1">
            <Field type="text" class="px-4 py-3 border-2 rounded-lg outline-none w-full" placeholder="Title (Optional)" id="title" name="title" v-model="formInput.title" />
            <ErrorMessage name="title" class="text-red-500" />
          </div>
          <div class="flex flex-col gap-2 flex-1">
            <Field type="text" class="px-4 py-3 border-2 rounded-lg outline-none w-full" placeholder="What's happening?" id="description" name="description" v-model="formInput.description" />
            <ErrorMessage name="description" class="text-red-500" />
          </div>
        </div>
        <div class="flex flex-col sm:flex-row gap-5">
          <div class="flex flex-col gap-2 flex-1">
            <Field type="text" class="px-4 py-3 border-2 rounded-lg outline-none w-full" placeholder="Tags (comma separated)" id="tags" name="tags" v-model="formInput.tags" />
            <ErrorMessage name="tags" class="text-red-500" />
          </div>
          <div class="flex flex-col gap-2 flex-1">
            <Field type="file" class="px-4 py-3 border-2 rounded-lg outline-none w-full" id="media" name="media" @change="handleMediaUpload" />
            <ErrorMessage name="media" class="text-red-500" />
          </div>
        </div>
        <div class="flex flex-col sm:flex-row gap-5">
          <div class="flex flex-col gap-2 flex-1">
            <Field type="text" class="px-4 py-3 border-2 rounded-lg outline-none w-full" placeholder="Location (Optional)" id="location" name="location" v-model="formInput.location" />
            <ErrorMessage name="location" class="text-red-500" />
          </div>
          <div class="flex flex-col gap-2 w-full sm:w-[10rem]">
            <select class="px-4 py-3 border-2 rounded-lg outline-none w-full" v-model="formInput.audience">
              <option value="public">Public</option>
              <option value="friends">Friends</option>
              <option value="group">Group</option>
            </select>
          </div>
        </div>
      </div>
      <div class="flex justify-end mt-6">
        <button type="submit" class="px-8 py-2 rounded-xl border-gray-300 bg-[#008A8A] text-white w-fit">
          Post
        </button>
      </div>
    </Form>
  </main>
</template>
